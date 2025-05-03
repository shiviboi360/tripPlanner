# trip_tasks.py (updated with proper flow)
from crewai import Task
from textwrap import dedent

class TripTasks:

    def identify_task(self, agent, origin, cities, interests, range):
        return Task(
            description=dedent(f"""
                Analyze and select the best city for the trip based on specific criteria such as weather patterns,
                seasonal events, and travel costs. Compare multiple cities, including weather, cultural events,
                and travel expenses.

                Final output must be a detailed report on the chosen city, including flight costs, weather forecast,
                and local attractions.

                Traveling from: {origin}
                City Options: {cities}
                Trip Date: {range}
                Traveler Interests: {interests}
            """),
            expected_output="A detailed report on the chosen city with flight costs, weather forecast, and attractions.",
            agent=agent
        )

    def gather_task(self, agent, origin, city, interests, range):
        return Task(
            description=dedent(f"""
                You are the local expert. Your job is to compile a comprehensive city guide for {city}. Include:

                Top attractions and activities
                Local customs and etiquette
                Events and festivals during the trip
                Weather expectations
                Approximate cost ranges (accommodation, food, transport)

                Trip Info:
                From: {origin}
                Dates: {range}
                Traveler Interests: {interests}

                Final Output: A cultural and practical guide for tourists with insider tips.
            """),
            expected_output="A cultural and practical city guide with local tips and activity options.",
            agent=agent
        )

    def plan_task(self, agent, origin, city, interests, range):
        return Task(
            description=dedent(f"""
                Your job is to build a detailed, day-wise travel itinerary for {city} from {range}.

                For each day, list:
                - Day number and title (e.g., Day 1: Arrival & Sunset Dinner)
                - Morning, Afternoon, and Evening activities
                - Restaurant and café suggestions
                - Weather forecast per day
                - Budget per day (optional split: Food, Travel, Tickets)
                - Packing suggestions if applicable

                Final Output: A markdown-formatted itinerary, broken down by day with detailed activities.
            """),
            expected_output="A complete markdown-formatted day-wise travel itinerary for the selected city, including daily activities, weather, food suggestions, budget, and packing tips."
                  ,agent=agent

        )
