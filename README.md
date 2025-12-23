# TalentScout – AI Hiring Assistant Chatbot

## Project Overview
TalentScout is an intelligent hiring assistant chatbot designed to support the **initial screening of candidates** for technical roles. The chatbot interacts with candidates in a conversational manner to collect essential profile details and dynamically generate **technology-specific interview questions** based on the candidate’s declared tech stack.

This project demonstrates effective use of **LLMs, prompt engineering, context management, and UI design** using Streamlit.

---

## Features
- Interactive chat-based UI using **Streamlit**
- Step-by-step candidate information collection
- Dynamic technical question generation based on tech stack
- Context-aware conversation flow using session state
- Robust fallback mechanism for LLM unavailability
- Input normalization for common technology name misspellings
- Graceful conversation termination
- Privacy-aware handling of candidate data (no persistence)

---

## Tech Stack
- **Programming Language:** Python  
- **Frontend:** Streamlit  
- **LLM:** OpenAI GPT (with rule-based fallback)  
- **Environment Management:** python-dotenv  

---

## Project Structure

```
talentscout-chatbot/
│
├── app.py # Streamlit UI & conversation flow
├── llm.py # LLM integration + fallback logic
├── conversation.py # Conversation flow & normalization
├── prompts.py # Prompt templates
├── requirements.txt
├── README.md
└── .env # API keys (not committed)
```


---

## Installation & Setup

### 1. Clone the repository

```
git clone <your-repo-url>
cd talentscout-chatbot
```

### 2. Create virtual environment

```
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Set environment variables

```
Create a .env file:

OPENAI_API_KEY=your_api_key_here
```

### 5. Run the application

```
streamlit run app.py
```

---

## How It Works (Conversation Flow)

1. Greets the candidate and explains the purpose

2. Collects candidate details sequentially:
    - Full Name
    - Email
    - Phone Number
    - Years of Experience
    - Desired Position
    - Location
    - Tech Stack

3. Normalizes noisy tech stack input (e.g., jango → Django)

4. Generates 3–5 technical questions per technology

5. Gracefully ends the conversation and disables further input

---

## Hosted On

[text](https://tschatbot.streamlit.app/)

---

## Prompt Design

- Separate prompts for information gathering and question generation

- Experience-aware prompts to ensure appropriate difficulty

- Clear instructions to avoid off-topic responses

- Deterministic fallback when LLM is unavailable

---

## Fallback & Error Handling

- If LLM quota is exceeded, the system switches to rule-based question generation

- Prevents duplicate question generation using session-state flags

- Handles unexpected inputs without deviating from the chatbot’s purpose

---

## Data Privacy & Compliance

- No database or file-based storage

- Candidate data exists only in Streamlit session memory

- No logging of personal or sensitive information

- GDPR-friendly simulated data handling

---

## Challenges & Solutions
```
| Challenge             | Solution                        |
| --------------------- | ------------------------------- |
| LLM quota limitations | Added rule-based fallback logic |
| Repeated responses    | Used session-state flags        |
| Noisy tech input      | Implemented normalization layer |
| Conversation overflow | Disabled input after completion |
```

---
## Future Enhancements

- Sentiment analysis during conversations

- Multilingual support

- Recruiter dashboard for reviewing candidates

- Cloud deployment (AWS / GCP)

---