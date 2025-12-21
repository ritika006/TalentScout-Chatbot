import os
from dotenv import load_dotenv

load_dotenv()

USE_OPENAI = True

try:
    from openai import OpenAI
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
except Exception:
    USE_OPENAI = False


def generate_technical_questions(tech_stack, experience):
    """
    Generates interview questions using OpenAI.
    Falls back to rule-based questions if quota is exceeded.
    """

    if USE_OPENAI:
        try:
            prompt = f"""
You are a senior technical interviewer.

Candidate experience: {experience} years
Tech Stack: {tech_stack}

Generate 3–5 interview questions for each technology.
Use bullet points.
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.4
            )

            return response.choices[0].message.content

        except Exception:
            pass  # fallback below

    # 🔁 FALLBACK (QUESTIONS ONLY)
    techs = [t.strip().title() for t in tech_stack.split(",")]

    output = ""
    for tech in techs:
        output += f"\n**{tech}**\n"
        output += f"- Explain the core concepts of {tech}.\n"
        output += f"- Describe a real-world project where you used {tech}.\n"
        output += f"- What are common challenges you faced while working with {tech}?\n"

    return output

