# 🏆 Microsoft Rewards Automation Bot

Fully automatic, headless Microsoft Rewards bot that:

- 🔎 Performs smart AI-generated Bing searches (desktop + mobile)
- 🎯 Completes Daily Set, Punch Cards, and basic Promotions
- 📊 Logs daily points into a history CSV
- 📈 Generates a points progress graph
- 📩 Sends Discord notifications after farming
- 🚀 Auto-starts on Windows at scheduled time
- 🎛️ Control Panel GUI (Start / Stop / Status)

---

## 📋 Features

| Feature | Status |
|:--------|:-------|
| Invisible Headless Browser (Edge) | ✅ |
| Smart Random AI Queries | ✅ |
| Auto Login or Skip if Already Connected | ✅ |
| Auto Complete Daily Sets | ✅ |
| Auto Complete Punch Cards (Searches & Quizzes) | ✅ |
| Auto Complete Other Promotions | ✅ |
| Points History Logging (`points_log.csv`) | ✅ |
| Points Progress Graph (with `graph_points.py`) | ✅ |
| Discord Notifications | ✅ |
| Auto-start with Windows Scheduler | ✅ |
| GUI Control Panel App (Tkinter) | ✅ |

---

## 🚀 How to Run

### 1. Manual Mode (Immediate Farming)

```bash
python main.py now
✅ Starts farming instantly (desktop and mobile searches, promotions, daily sets).

2. Auto Daily Farming (Scheduled)
Auto-start at PC boot using Windows Task Scheduler.

Launches farming daily at configured time (example: 8:00 AM).

🛠 Installation
Clone this repo or copy the project locally.

Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Configure:

config/accounts.json → Add your Microsoft accounts.

config/settings.json → Customize region, Discord webhook, smart mode, farming time.

Run and start farming!

📚 Directory Structure
bash
Copy
Edit
microsoft_rewards_bot/
│
├── config/
│   ├── accounts.json
│   ├── settings.json
│   └── search_topics.txt
│
├── scripts/
│   ├── browser_manager.py
│   ├── login_manager.py
│   ├── searcher.py
│   ├── promotions.py
│   ├── notifier.py
│   ├── utils.py
│   ├── points_logger.py
│   └── query_generator.py
│
├── control_panel.py    # 🎛️ GUI app
├── graph_points.py     # 📈 Points graph generator
├── main.py             # 🧠 Bot launcher
└── points_log.csv      # 📊 Points history file
📄 Notes
✅ Works with multiple accounts.

✅ Fully headless — no browser windows visible during farming.

✅ Smarter search queries to avoid detection.

✅ Logs each day's total points for historical tracking.

✅ Sends success notifications to Discord automatically.

🎯 Future Work (Optional)
CAPTCHA auto-solving (coming later if needed)

Advanced quiz correct-answer prediction

Telegram phone notifications

If you wanna help me out use my refferal link to sign up:
https://rewards.bing.com/welcome?rh=F8AC64A6&ref=rafsae

🧠 Credits
Developed by shaggylaggyy 🧠🚀
