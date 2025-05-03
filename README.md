# 👛 AI Trip Planner with CrewAI + Streamlit

Let AI agents plan your dream vacation—city selection, cultural guide, and detailed itineraries included!

## ✨ Overview

This project is an AI-powered travel planning assistant built using [CrewAI](https://github.com/joaomdmoura/crewAI), [Streamlit](https://streamlit.io/), and Langchain-compatible tools. It uses autonomous agents to:

* Select the best destination based on your input
* Provide cultural and cost insights
* Generate a detailed day-by-day itinerary

### ✅ What It Does

* Takes in:

  * Origin city
  * Destination options
  * Travel dates
  * Interests (e.g. food, beaches, hiking)
* Uses CrewAI agents to:

  1. **Select the most suitable city** (weather, events, travel cost)
  2. **Generate a cultural and practical guide** for that city
  3. **Create a full 3–7 day itinerary** including weather, restaurants, budget, and packing tips

## 🧠 Tech Stack

* **Frontend**: Streamlit
* **AI Framework**: CrewAI with Langchain-style agents
* **LLM Access**: OpenAI via API (hidden via `.streamlit/secrets.toml`)
* **Tools Integrated**:

  * Serper.dev (Google Search)
  * Browserless (Web scraping)
  * Optional: OpenRouter or Gemini LLMs for free inference

## 🔩 Agent Structure

| Agent            | Role                            |
| ---------------- | ------------------------------- |
| City Selector    | Analyzes cities for your trip   |
| Local Expert     | Compiles guide on local culture |
| Travel Concierge | Crafts a daily itinerary        |

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/shiviboi360/tripPlanner.git
cd tripPlanner
```

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Set Your API Keys

Create a `.streamlit/secrets.toml` file (this file is gitignored):

```toml
SERPER_API_KEY = "your-serper-key"
BROWSERLESS_API_KEY = "your-browserless-key"
OPENAI_API_KEY = "your-openai-key"
```

### 4. Run the App

```bash
streamlit run streamlit_app.py
```

## 🖼️ Screenshots

## 🛡️ Security

This repo is protected from accidental API key leaks using:

* `.gitignore` for `secrets.toml`
* GitHub Push Protection (GH013)

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤛‍♂️ Author

**Shravan Sailada**
Connect: [LinkedIn](https://www.linkedin.com/in/shravan-sailada/) | [Twitter](https://twitter.com/)
