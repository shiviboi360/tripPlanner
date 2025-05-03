# streamlit_app.py (updated)
import datetime
import sys
import streamlit as st

from crewai import Crew
from trip_agents import TripAgents, StreamToExpander
from trip_tasks import TripTasks

st.set_page_config(page_icon="✈️", layout="wide")

def icon(emoji: str):
    st.write(
        f'<span style="font-size: 78px; line-height: 1">{emoji}</span>',
        unsafe_allow_html=True,
    )

class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests
        self.output_placeholder = st.empty()

    def run(self):
        agents = TripAgents()
        tasks = TripTasks()

        city_selector = agents.city_selection_agent()
        local_expert = agents.local_expert()
        travel_concierge = agents.travel_concierge()

        identify_task = tasks.identify_task(
            agent=city_selector,
            origin=self.origin,
            cities=self.cities,
            interests=self.interests,
            range=self.date_range,
        )

        # Use the first city from the list or string for now
        selected_city = self.cities.split(",")[0].strip() if "," in self.cities else self.cities.strip()

        gather_task = tasks.gather_task(
            agent=local_expert,
            origin=self.origin,
            city=selected_city,
            interests=self.interests,
            range=self.date_range,
        )

        plan_task = tasks.plan_task(
            agent=travel_concierge,
            origin=self.origin,
            city=selected_city,
            interests=self.interests,
            range=self.date_range,
        )

        crew = Crew(
            agents=[city_selector, local_expert, travel_concierge],
            tasks=[identify_task, gather_task, plan_task],
            verbose=True,
        )

        result = crew.kickoff()
        self.output_placeholder.markdown(result)
        return result

# --- Streamlit UI ---

if __name__ == "__main__":
    icon("🏖️ VacAIgent")

    st.subheader("Let AI agents plan your next vacation!", divider="rainbow", anchor=False)

    today = datetime.date.today()
    next_year = today.year + 1
    default_end_date = datetime.date(next_year, 1, 16)

    with st.sidebar:
        st.header("👇 Enter your trip details")
        with st.form("trip_form"):
            location = st.text_input("Where are you currently located?", placeholder="San Mateo, CA")
            cities = st.text_input("City/country you want to visit?", placeholder="Bali, Indonesia")
            date_range = st.date_input(
                "Travel date range",
                min_value=today,
                value=(today, default_end_date),
                format="MM/DD/YYYY",
            )
            interests = st.text_area(
                "Travel interests or extra info",
                placeholder="2 adults who love swimming, dancing, hiking, and eating"
            )
            submitted = st.form_submit_button("Submit")

    if submitted:
        stream_expander = StreamToExpander(st)

        with st.status("🤖 **Agents at work...**", state="running", expanded=True) as status:
            original_stdout = sys.stdout
            sys.stdout = stream_expander
            try:
                trip_crew = TripCrew(location, cities, date_range, interests)
                result = trip_crew.run()
            finally:
                sys.stdout = original_stdout

            status.update(label="✅ Trip Plan Ready!", state="complete", expanded=False)

        st.subheader("Here is your Trip Plan", anchor=False, divider="rainbow")
        st.markdown(result)

    st.markdown("---")
    st.caption("Powered by [CrewAI](https://github.com/joaomdmoura/crewAI) by [@joaomdmoura](https://twitter.com/joaomdmoura) 🚀")
