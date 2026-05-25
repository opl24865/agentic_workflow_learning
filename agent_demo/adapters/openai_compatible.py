from openai import OpenAI
from .base import BaseAdapter

class OpenAICompatibleAdapter(BaseAdapter):
    def __init__(self, model: str, api_key: str, base_url: str):
        self.model = model
        self.client = OpenAI(
            api_key=api_key,
            base_url=base_url
        )
    
    def chat(self, messages, tools=None):
        params = {
            "model": self.model,
            "messages": messages,
            "temperature": 0
        }

        if tools:
            params["tools"] = tools
            params["tool_choice"] = "auto"
        
        rsp = self.client.chat.completions.create(**params)
        msg = rsp.choices[0].message

        return {
            "message": msg.model_dump()
        }