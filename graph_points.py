import pandas as pd
import matplotlib.pyplot as plt

def plot_points_history():
    try:
        df = pd.read_csv("points_log.csv", header=None, names=["Date", "Points"])
        df["Date"] = pd.to_datetime(df["Date"])
        df = df.sort_values(by="Date")

        plt.figure(figsize=(10, 6))
        plt.plot(df["Date"], df["Points"], marker="o")
        plt.title("Microsoft Rewards Points History")
        plt.xlabel("Date")
        plt.ylabel("Points")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"❌ Failed to plot points history: {e}")

if __name__ == "__main__":
    plot_points_history()
