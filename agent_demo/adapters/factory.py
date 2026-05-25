# 集中管理要用哪個模型

import os
from .openai_compatible import OpenAICompatibleAdapter

def get_adapter(provider: str):
    if provider == 'deepseek':
        return OpenAICompatibleAdapter(
            model='deepseek-chat',
            api_key = os.getenv("DEEPSEEK_API_KEY"),
            base_url = "https://api.deepseek.com"
        )
    
    if provider == 'Groq':
        return OpenAICompatibleAdapter(
            model="llama-3.1-8b-instant",
            api_key=os.getenv("GROQ_API_KEY"),
            base_url="https://api.groq.com/openai/v1"
        )
    
    if provider == 'ollama':
        return OpenAICompatibleAdapter(
            model="qwen3-coder:480b-cloud",
            api_key=os.getenv("OLLAMA_API_KEY"),
            base_url = "http://localhost:11434/v1"
        )
    
    if provider == "vllm":
        return OpenAICompatibleAdapter(
            model=os.getenv("VLLM_MODEL", "Qwen2.5-7B-Instruct"),
            api_key="EMPTY",
            base_url="http://localhost:8000/v1"
        )
    
    raise ValueError(f"Unknown provider: {provider}")