CANDIDATE_FIELDS = [
    ("full_name", "What is your full name?"),
    ("email", "Please provide your email address."),
    ("phone", "What is your phone number?"),
    ("experience", "How many years of experience do you have?"),
    ("position", "What position are you applying for?"),
    ("location", "What is your current location?"),
    ("tech_stack", "Please list your tech stack (languages, frameworks, tools)."),
]

EXIT_KEYWORDS = ["exit", "quit", "bye", "stop"]


def get_next_question(candidate_data):
    """
    Returns the next question to ask based on missing candidate data.
    """
    for field, question in CANDIDATE_FIELDS:
        if field not in candidate_data:
            return question
    return None

TECH_CORRECTIONS = {
    # Python
    "python": "Python",
    "pyhton": "Python",
    "puthon": "Python",
    "phyton": "Python",

    # Django
    "django": "Django",
    "jango": "Django",
    "djanga": "Django",

    # Flask
    "flask": "Flask",
    "flaskk": "Flask",

    # JS ecosystem
    "js": "JavaScript",
    "javascript": "JavaScript",
    "node": "Node.js",
    "nodejs": "Node.js",
    "react": "React",
    "reactjs": "React",
}

def normalize_tech_stack(tech_stack):
    cleaned = []

    for tech in tech_stack.split(","):
        tech_key = tech.strip().lower()

        if tech_key in TECH_CORRECTIONS:
            cleaned.append(TECH_CORRECTIONS[tech_key])
        else:
            cleaned.append(tech_key.title())

    return ", ".join(cleaned)

