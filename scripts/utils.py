import random
import json

def get_random_greeting():
    greetings = [
        "🌞 Good morning! Let's farm some points!",
        "🌙 Good evening! Time to earn rewards!",
        "🔥 Ready to smash today's farming session!",
        "🚀 Starting today's Microsoft Rewards journey!",
        "🏆 Time to collect those points!"
    ]
    return random.choice(greetings)

def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def load_search_topics(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]
