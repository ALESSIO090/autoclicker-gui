import pyautogui
import threading
import time
import tkinter as tk
from tkinter import messagebox

clicking = False
delay = 0.1

def start_clicking():
    global clicking
    clicking = True
    status_label.config(text="Status: ACTIVE")

def stop_clicking():
    global clicking
    clicking = False
    status_label.config(text="Status: Paused")

def set_speed():
    global delay
    try:
        value = float(speed_entry.get())
        delay = value
        status_label.config(text=f"Speed set to: {delay} sec")
    except ValueError:
        status_label.config(text="Error: Enter a valid number")

def click_loop():
    while True:
        if clicking:
            pyautogui.click()
            time.sleep(delay)
        else:
            time.sleep(0.1)

def toggle_fullscreen(event=None):
    global is_fullscreen
    is_fullscreen = not is_fullscreen
    root.attributes("-fullscreen", is_fullscreen)
    if not is_fullscreen:
        root.iconify()

def exit_app(event=None):
    root.quit()

# Background click thread
threading.Thread(target=click_loop, daemon=True).start()

# GUI setup
root = tk.Tk()
root.title("Autoclicker")
root.geometry("400x300")
is_fullscreen = False

tk.Label(root, text="Click Interval (sec):").pack(pady=5)
speed_entry = tk.Entry(root)
speed_entry.insert(0, "0.1")
speed_entry.pack(pady=5)

start_btn = tk.Button(root, text="Start", command=start_clicking, bg="green", fg="white")
start_btn.pack(pady=5)

stop_btn = tk.Button(root, text="Stop", command=stop_clicking, bg="red", fg="white")
stop_btn.pack(pady=5)

set_btn = tk.Button(root, text="Set Speed", command=set_speed)
set_btn.pack(pady=5)

status_label = tk.Label(root, text="Status: Ready")
status_label.pack(pady=10)

root.bind("<F11>", toggle_fullscreen)
root.bind("<Escape>", exit_app)

root.mainloop()
