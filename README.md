<p align="center">
  <img src="https://img.shields.io/github/license/shaggylaggyy/microsoft-rewards-bot?color=brightgreen&style=for-the-badge" alt="License">
  <img src="https://img.shields.io/github/stars/shaggylaggyy/microsoft-rewards-bot?color=yellow&style=for-the-badge" alt="Stars">
  <img src="https://img.shields.io/github/forks/shaggylaggyy/microsoft-rewards-bot?color=blue&style=for-the-badge" alt="Forks">
  <img src="https://img.shields.io/github/issues/shaggylaggyy/microsoft-rewards-bot?color=red&style=for-the-badge" alt="Issues">
  <img src="https://img.shields.io/github/last-commit/shaggylaggyy/microsoft-rewards-bot?color=purple&style=for-the-badge" alt="Last Commit">
  <img src="https://img.shields.io/badge/Python-3.11%2B-blue?style=for-the-badge&logo=python" alt="Python">
  <img src="https://img.shields.io/badge/Made%20With-Selenium-brightgreen?style=for-the-badge&logo=selenium" alt="Selenium">
  <img src="https://img.shields.io/badge/Edge-Automation-blue?style=for-the-badge&logo=microsoftedge" alt="Microsoft Edge">
</p>

<h1 align="center">🏆 Microsoft Rewards Automation Bot</h1>


## A powerful bot to fully automate Microsoft Rewards farming with Daily Set, Promotions, Searches and Discord notifications! 🚀

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

# 📦 Installation

> Ensure you have **Python 3.11+** installed before starting.

1. Clone the repository:
```bash
git clone https://github.com/shaggylaggyy/microsoft-rewards-bot.git
```
2. Install the dependencies:
```bash
pip install -r requirements.txt
```
3. Configure your Microsoft accounts inside:
```bash
config/accounts.json
```
4. Run the bot:
```bash
python main.py
```

---

# 🛡️ Security Notice

> This project is intended for **educational purposes only**.
> Use responsibly and within the Microsoft Rewards guidelines.
> Review Microsoft's Terms of Service before using automation tools.
> The author is **not responsible** for any misuse or consequences.

---

# 🏷️ Version

- **v1.0** — Initial full bot release:
  - Interactive Task Selection 🏫
  - Daily Set Automation ✅
  - Punch Cards Completion ✅
  - Promotions Collection ✅
  - Desktop + Mobile Searches ✅
  - Discord Webhook Notifications ✅
  - Clean Headless Mode Operation ✅

---

# 🚀 Roadmap

- [x] Interactive Task Control Panel
- [x] Clean Silent Farming (Headless Mode)
- [x] Professional Discord Notifications
- [ ] 🔜 Captcha Auto-Solver Integration
- [ ] 🔜 Smart Quiz Auto-Answering
- [ ] 🔜 Random Human-Like Movements (Stealth Farming)
- [ ] 🔜 Auto Daily Scheduled Farming (Task Scheduler integration)
- [ ] 🔜 Web Dashboard Control Panel (Streamlit/Tkinter)

---

## 📁 Directory Structure

```
microsoft_rewards_bot/
├── config/
│   ├── accounts.json
│   ├── settings.json
│   └── search_topics.txt
├── scripts/
│   ├── browser_manager.py
│   ├── login_manager.py
│   ├── searcher.py
│   ├── promotions.py
│   ├── notifier.py
│   ├── utils.py
│   ├── points_logger.py
│   └── query_generator.py
├── control_panel.py      # 🧩 GUI app
├── graph_points.py       # 📊 Points graph generator
├── main.py               # 🧠 Bot launcher
├── points_log.csv        # 📚 Points history file
├── README.md             # 📝 Project documentation
├── LICENSE               # 📜 MIT license
└── requirements.txt      # 📦 Python dependencies
```

---

📄 Notes
✅ Works with multiple accounts.

✅ Fully headless — no browser windows visible during farming.

✅ Smarter search queries to avoid detection.

✅ Logs each day's total points for historical tracking.

✅ Sends success notifications to Discord automatically.

---

# ❤️ Credits

Made with ❤️ by [**shaggylaggyy**](https://github.com/shaggylaggyy)

> Contributions are welcome! Feel free to open pull requests or suggestions 💛
