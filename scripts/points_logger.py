import csv
from datetime import datetime

def log_points(points_today):
    filename = "points_log.csv"
    today = datetime.now().strftime("%Y-%m-%d")
    try:
        with open(filename, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([today, points_today])
        print(f"📊 Points logged: {points_today} points on {today}")
    except Exception as e:
        print(f"❌ Failed to log points: {e}")
