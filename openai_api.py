import openai

class OpenAI_API:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_response(self, prompt, engine, max_tokens, temperature):
        # Задаем параметры запроса
        prompt = (prompt.strip() + "\n").replace("\n", "\nModel:")
        completions = openai.Completion.create(
            engine=engine,
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature,
        )

        # Обрабатываем ответ и возвращаем результат
        message = completions.choices[0].text
        return message.strip()
