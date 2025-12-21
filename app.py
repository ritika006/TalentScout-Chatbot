import conversation
import streamlit as st
from conversation import get_next_question, EXIT_KEYWORDS
from llm import generate_technical_questions

if "questions_generated" not in st.session_state:
    st.session_state.questions_generated = False

if "conversation_ended" not in st.session_state:
    st.session_state.conversation_ended = False

st.set_page_config(
    page_title="TalentScout Hiring Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 TalentScout Hiring Assistant")
st.write(
    "Hi! I will assist with your initial screening by collecting some information "
    "and then asking technical questions based on your tech stack."
)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "candidate_data" not in st.session_state:
    st.session_state.candidate_data = {}

# Initial greeting
if not st.session_state.messages:
    first_question = get_next_question(st.session_state.candidate_data)
    st.session_state.messages.append(
        {"role": "assistant", "content": first_question}
    )

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
if not st.session_state.conversation_ended:
    user_input = st.chat_input("Type your response here...")
else:
    user_input = None

if user_input:
    # Exit condition
    if user_input.lower().strip() in EXIT_KEYWORDS:
        st.session_state.messages.append(
            {"role": "assistant", "content": "Thank you for your time. Goodbye!"}
        )
        st.rerun()

    # Store user message
    st.session_state.messages.append(
        {"role": "user", "content": user_input}
    )

    # Save answer to next missing field
    for field, _ in conversation.CANDIDATE_FIELDS:
        if field not in st.session_state.candidate_data:
            if field == "tech_stack":
                from conversation import normalize_tech_stack
                st.session_state.candidate_data[field] = normalize_tech_stack(user_input)
            else:
                st.session_state.candidate_data[field] = user_input

            break

    # Ask next question
    next_question = get_next_question(st.session_state.candidate_data)

    if next_question:
        st.session_state.messages.append(
            {"role": "assistant", "content": next_question}
        )
    else:
        if not st.session_state.questions_generated:
            tech_stack = st.session_state.candidate_data.get("tech_stack")
            experience = st.session_state.candidate_data.get("experience")

            questions = generate_technical_questions(tech_stack, experience)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": "Thank you! Based on your tech stack, here are some technical questions:"
                }
            )

            st.session_state.messages.append(
                {"role": "assistant", "content": questions}
            )

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": (
                        "This concludes the initial screening.\n\n"
                        "Please make a note of these questions. Our recruitment team will review "
                        "your profile and discuss them with you in the next round.\n\n"
                        "Thank you for your time!"

                    )
                }
            )

            st.session_state.questions_generated = True
            st.session_state.conversation_ended = True


    st.rerun()
