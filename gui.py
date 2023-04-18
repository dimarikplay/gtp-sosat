import tkinter as tk
from tkinter import scrolledtext

from app import ChatApp
from user_input import UserInput
from message import ChatMessage


class ChatGUI:
    def __init__(self, chat_app: ChatApp):
        self.chat_app = chat_app
        self.window = tk.Tk()
        self.window.title("OpenAI Chat")
        self.chat_history = scrolledtext.ScrolledText(self.window, state='disabled')
        self.user_input = UserInput(self.window, self.generate_response)
        self.chat_history.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.user_input.pack(side=tk.BOTTOM, fill=tk.X)

    def run(self):
        self.window.mainloop()

    def generate_response(self, message):
        response = self.chat_app.generate_response(message)
        chat_message = ChatMessage(message, response)
        self.chat_history.configure(state='normal')
        self.chat_history.insert(tk.END, chat_message.to_string() + "\n")
        self.chat_history.configure(state='disabled')
        self.chat_history.see(tk.END)
