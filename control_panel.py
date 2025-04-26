import subprocess
import tkinter as tk
import os
import signal

# Track bot process
bot_process = None

def start_farming():
    global bot_process
    if bot_process is None:
        bot_process = subprocess.Popen(["python", "main.py", "now"], creationflags=subprocess.CREATE_NEW_CONSOLE)
        status_label.config(text="✅ Bot is running...")
    else:
        status_label.config(text="⚠️ Bot already running!")

def view_status():
    if bot_process is not None and bot_process.poll() is None:
        status_label.config(text="✅ Bot is still running.")
    else:
        status_label.config(text="⛔ Bot is not running.")

def stop_farming():
    global bot_process
    if bot_process is not None:
        os.kill(bot_process.pid, signal.SIGTERM)
        bot_process = None
        status_label.config(text="🛑 Bot stopped.")
    else:
        status_label.config(text="⚠️ No bot to stop.")

def exit_app():
    stop_farming()
    root.destroy()

# Create GUI
root = tk.Tk()
root.title("Microsoft Rewards Bot Control Panel")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

title_label = tk.Label(root, text="Microsoft Rewards Bot", font=("Arial", 20), bg="#f0f0f0")
title_label.pack(pady=20)

start_button = tk.Button(root, text="🏁 Start Farming", font=("Arial", 14), width=20, command=start_farming)
start_button.pack(pady=10)

status_button = tk.Button(root, text="📄 View Status", font=("Arial", 14), width=20, command=view_status)
status_button.pack(pady=10)

stop_button = tk.Button(root, text="🛑 Stop Bot", font=("Arial", 14), width=20, command=stop_farming)
stop_button.pack(pady=10)

exit_button = tk.Button(root, text="❌ Exit", font=("Arial", 14), width=20, command=exit_app)
exit_button.pack(pady=10)

status_label = tk.Label(root, text="Waiting...", font=("Arial", 12), bg="#f0f0f0")
status_label.pack(pady=20)

root.mainloop()
