# trip_agents.py

import os
import re
import streamlit as st
from crewai import Agent
from langchain_openai import ChatOpenAI

from tools.search_tools import InternetSearchTool
from tools.browser_tools import BrowserScrapeTool
from tools.calculator_tools import TripBudgetCalculatorTool


class TripAgents:
    def __init__(self):
        os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]
        self.llm = ChatOpenAI(model="gpt-3.5-turbo")

        # Initialize tools once
        self.search_tool = InternetSearchTool()
        self.scrape_tool = BrowserScrapeTool()
        self.calc_tool = TripBudgetCalculatorTool()

    def city_selection_agent(self):
        return Agent(
            role="City Selection Expert",
            goal="Select the best city based on weather, season, and prices",
            backstory="An expert in analyzing travel data to pick ideal destinations.",
            tools=[self.search_tool, self.scrape_tool],
            verbose=True,
            llm=self.llm
        )

    def local_expert(self):
        return Agent(
            role="Local Expert",
            goal="Provide deep insights about the selected city, its customs, and highlights.",
            backstory="A local guide with cultural and practical knowledge of the city.",
            tools=[self.search_tool, self.scrape_tool],
            verbose=True,
            llm=self.llm
        )

    def travel_concierge(self):
        return Agent(
            role="Travel Concierge",
            goal="Create efficient and budget-conscious itineraries including packing suggestions.",
            backstory="A planner skilled in balancing time, cost, and experience quality.",
            tools=[self.search_tool, self.scrape_tool, self.calc_tool],
            verbose=True,
            llm=self.llm
        )


class StreamToExpander:
    def __init__(self, st_module):
        self.expander = st_module.expander("Agent Logs", expanded=True)
        self.buffer = []
        self.colors = ['red', 'green', 'blue', 'orange']
        self.color_index = 0

    def write(self, data):
        import re
        cleaned = re.sub(r'\x1B\[[0-9;]*[mK]', '', data)
        if "Entering new CrewAgentExecutor chain" in cleaned:
            self.color_index = (self.color_index + 1) % len(self.colors)
            cleaned = cleaned.replace(
                "Entering new CrewAgentExecutor chain",
                f":{self.colors[self.color_index]}[Entering new CrewAgentExecutor chain]"
            )
        self.buffer.append(cleaned)
        if "\n" in data:
            self.expander.markdown(''.join(self.buffer), unsafe_allow_html=True)
            self.buffer = []

    def flush(self):
        pass  # Required by sys.stdout compatibility

