from pydantic import BaseModel, Field
from typing import Type
from unstructured.partition.html import partition_html
from crewai.tools import BaseTool
from langchain_openai import ChatOpenAI
import streamlit as st
import json
import requests

class BrowserScrapeInput(BaseModel):
    website: str = Field(..., description="The URL of the website to scrape and summarize.")

class BrowserScrapeTool(BaseTool):
    name: str = "Scrape Website Tool"
    description: str = "Scrape and summarize a webpage using Browserless API and CrewAI."
    args_schema: Type[BaseModel] = BrowserScrapeInput

    def _run(self, website: str) -> str:
        try:
            url = f"https://chrome.browserless.io/content?token={st.secrets['BROWSERLESS_API_KEY']}"
            payload = json.dumps({"url": website})
            headers = {
                'cache-control': 'no-cache',
                'content-type': 'application/json'
            }
            response = requests.post(url, headers=headers, data=payload)

            elements = partition_html(text=response.text)
            content = "\n\n".join([str(el) for el in elements])
            chunks = [content[i:i + 8000] for i in range(0, len(content), 8000)]

            # ✅ Avoid self.llm: create LLM inside the function
            llm = ChatOpenAI(model="gpt-3.5-turbo")
            summaries = []
            for chunk in chunks:
                summary = llm.invoke(f"Summarize this webpage content:\n{chunk}")
                summaries.append(summary.content)

            return "\n\n".join(summaries)

        except Exception as e:
            return f"❌ Error during scraping: {str(e)}"
