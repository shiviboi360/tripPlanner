# tools/search_tools.py

import os
import streamlit as st
import requests
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

class InternetSearchInput(BaseModel):
    query: str = Field(..., description="Search query string to look up online")

class InternetSearchTool(BaseTool):
    name: str = "Internet Search Tool"
    description: str = "Search the internet for the given query using the Serper.dev API."
    args_schema: Type[BaseModel] = InternetSearchInput

    def _run(self, query: str) -> str:
        try:
            api_key = st.secrets["SERPER_API_KEY"]
            if not api_key:
                return "❌ SERPER_API_KEY not found in environment variables."
            headers = {
                "X-API-KEY": api_key,
                "Content-Type": "application/json"
            }
            payload = {
                "q": query,
                "gl": "us",
                "hl": "en"
            }
            response = requests.post("https://google.serper.dev/search", headers=headers, json=payload)
            response.raise_for_status()
            data = response.json()
            results = data.get("organic", [])
            if not results:
                return "No relevant results found."
            top_results = [f"{item.get('title', '')}: {item.get('link', '')}" for item in results[:3]]
            return "\n".join(top_results)
        except Exception as e:
            return f"❌ Error during search: {str(e)}"
