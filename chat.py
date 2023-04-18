from tkinter import scrolledtext
import datetime

class Chat:
    def __init__(self, chat_frame):
        self.chat_frame = chat_frame
        self.chat_history = scrolledtext.ScrolledText(chat_frame, wrap="word")
        self.chat_history.grid(row=0, column=0, sticky="nsew")

    def add_message(self, message, sender="AI"):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.chat_history.insert("end", f"[{timestamp}] {sender}: {message}\n")
        self.chat_history.see("end")
