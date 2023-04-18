import tkinter as tk

class UserInput:
    def __init__(self, params_frame, response_frame, openai_api):
        self.params_frame = params_frame
        self.response_frame = response_frame
        self.openai_api = openai_api

        # Создание виджетов для параметров запроса
        tk.Label(params_frame, text="Движок:").grid(row=0, column=0, sticky="w")
        self.engine_var = tk.StringVar()
        engine_options = ["davinci", "curie", "babbage", "ada"]
        self.engine_var.set(engine_options[0])
        engine_dropdown = tk.OptionMenu(params_frame, self.engine_var, *engine_options)
        engine_dropdown.grid(row=0, column=1)

        tk.Label(params_frame, text="Промт:").grid(row=1, column=0, sticky="w")
        self.prompt_entry = tk.Entry(params_frame, width=50)
        self.prompt_entry.grid(row=1, column=1)

        tk.Label(params_frame, text="Максимальное количество токенов:").grid(row=2, column=0, sticky="w")
        self.max_tokens_entry = tk.Entry(params_frame, width=10)
        self.max_tokens_entry.insert(0, "150")
        self.max_tokens_entry.grid(row=2, column=1)

        tk.Label(params_frame, text="Количество ответов:").grid(row=3, column=0, sticky="w")
        self.n_entry = tk.Entry(params_frame, width=5)
        self.n_entry.insert(0, "1")
        self.n_entry.grid(row=3, column=1)

        tk.Label(params_frame, text="Стоп слова:").grid(row=4, column=0, sticky="w")
        self.stop_entry = tk.Entry(params_frame, width=50)
        self.stop_entry.grid(row=4, column=1)

        tk.Label(params_frame, text="Температура:").grid(row=5, column=0, sticky="w")
        self.temperature_entry = tk.Entry(params_frame, width=5)
        self.temperature_entry.insert(0, "0.5")
        self.temperature_entry.grid(row=5, column=1)

        # Создание кнопки для отправки запроса
        submit_button = tk.Button(params_frame, text="Отправить", command=self.generate_response)
        submit_button.grid(row=6, column=0, columnspan=2)

        # Создание виджетов для вывода ответа
        self.response_text = tk.Text(response_frame, height=20, width=80)
        self.response_text.pack()

    def generate_response(self):
        engine = self.engine_var.get()
        prompt = self.prompt_entry.get()
        max_tokens = int(self.max_tokens_entry.get())
        n = int(self.n_entry.get())
        stop = self.stop_entry.get().split(",")
        temperature = float(self.temperature_entry.get())

        response = self.openai_api.generate_response(engine, prompt, max_tokens, n, stop, temperature)

        self.response_text.delete("1.0", tk.END)
        for message in response:
            self.response_text.insert(tk.END, f"{message.sender}: {message.text}\n\n")
import tkinter as tk

class UserInput:
    def __init__(self, params_frame, response_frame, openai_api):
        self.params_frame = params_frame
        self.response_frame = response_frame
        self.openai_api = openai_api

        # Создание виджетов для параметров запроса
        tk.Label(params_frame, text="Движок:").grid(row=0, column=0, sticky="w")
        self.engine_var = tk.StringVar()
        engine_options = ["davinci", "curie", "babbage", "ada"]
        self.engine_var.set(engine_options[0])
        engine_dropdown = tk.OptionMenu(params_frame, self.engine_var, *engine_options)
        engine_dropdown.grid(row=0, column=1)

        tk.Label(params_frame, text="Промт:").grid(row=1, column=0, sticky="w")
        self.prompt_entry = tk.Entry(params_frame, width=50)
        self.prompt_entry.grid(row=1, column=1)

        tk.Label(params_frame, text="Максимальное количество токенов:").grid(row=2, column=0, sticky="w")
        self.max_tokens_entry = tk.Entry(params_frame, width=10)
        self.max_tokens_entry.insert(0, "150")
        self.max_tokens_entry.grid(row=2, column=1)

        tk.Label(params_frame, text="Количество ответов:").grid(row=3, column=0, sticky="w")
        self.n_entry = tk.Entry(params_frame, width=5)
        self.n_entry.insert(0, "1")
        self.n_entry.grid(row=3, column=1)

        tk.Label(params_frame, text="Стоп слова:").grid(row=4, column=0, sticky="w")
        self.stop_entry = tk.Entry(params_frame, width=50)
        self.stop_entry.grid(row=4, column=1)

        tk.Label(params_frame, text="Температура:").grid(row=5, column=0, sticky="w")
        self.temperature_entry = tk.Entry(params_frame, width=5)
        self.temperature_entry.insert(0, "0.5")
        self.temperature_entry.grid(row=5, column=1)

        # Создание кнопки для отправки запроса
        submit_button = tk.Button(params_frame, text="Отправить", command=self.generate_response)
        submit_button.grid(row=6, column=0, columnspan=2)

        # Создание виджетов для вывода ответа
        self.response_text = tk.Text(response_frame, height=20, width=80)
        self.response_text.pack()

    def generate_response(self):
        engine = self.engine_var.get()
        prompt = self.prompt_entry.get()
        max_tokens = int(self.max_tokens_entry.get())
        n = int(self.n_entry.get())
        stop = self.stop_entry.get().split(",")
        temperature = float(self.temperature_entry.get())

        response = self.openai_api.generate_response(engine, prompt, max_tokens, n, stop, temperature)

        self.response_text.delete("1.0", tk.END)
        for message in response:
            self.response_text.insert(tk.END, f"{message.sender}: {message.text}\n\n")
