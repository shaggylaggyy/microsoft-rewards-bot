import random
from datetime import datetime

buzzwords = [
    "trending", "latest", "best", "top", "ideas", "2025", "today", "this week", "new", "future", "top rated"
]

def generate_smart_query(base_topic):
    year = datetime.now().year
    additions = [
        f"{random.choice(buzzwords)}",
        f"{year}",
        f"how to {base_topic.lower()}",
        f"{base_topic.lower()} tips",
        f"{base_topic.lower()} {random.choice(buzzwords)} {year}",
        f"{base_topic.lower()} guide {year}"
    ]
    return f"{base_topic} {random.choice(additions)}"
