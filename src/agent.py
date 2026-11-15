import os
from dotenv import load_dotenv
from openai import OpenAI

# Загружаем переменные окружения из .env
load_dotenv()

SYSTEM_PROMPT = """
You are a helpful, polite, and professional Smart Customer Support Agent for an e-commerce store.
Your job is to assist customers with order tracking, store return/shipping policies, and general inquiries.
Always be concise, empathetic, and clear. If a request requires looking up private order data or store rules, 
acknowledge the request professionally.
"""


class SupportAgent:
    def __init__(self, model: str | None = None):
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            raise ValueError("OPENROUTER_API_KEY is not set in environment variables.")
        
        self.model = model or os.getenv("MODEL_NAME", "openai/gpt-4o-mini")
        self.client = OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=api_key,
        )

    def ask(self, user_message: str) -> str:
        """Отправляет базовый запрос пользователя в LLM через OpenRouter и возвращает ответ."""
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content


if __name__ == "__main__":
    agent = SupportAgent()
    test_query = "Hi! I ordered a laptop yesterday (ORD-1001). How can I check its status?"
    print(f"Model: {agent.model}")
    print(f"User: {test_query}\n")
    print(f"Agent: {agent.ask(test_query)}")