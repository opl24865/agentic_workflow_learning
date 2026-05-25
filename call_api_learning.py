from email import message
from openai import OpenAI
import os

BASE_URL = "https://api.deepseek.com"
API_key = os.getenv("DEEPSEEK_API_KEY")



client = OpenAI(
    api_key = API_key,
    base_url = BASE_URL
)

resp = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {"role": "system", "content": "你是專業的AI助手"},
        {"role": "user", "content": "請用三點說明什麼是RAG"}
    ],
    temperature = 0.2
)


resp_jons = client.chat.completions.create(
    model = "deepseek-chat",
    messages = [
        {
            "role": "user",
            "content": "請用 JSON 輸出：模型名稱、用途、優點、缺點"
        }
    ],
    response_format = {"type": "json_object"}
)

# print(resp_jons.choices[0].message.content)



messages = [
    {
        "role": "system",
        "content": "你是專業 AI 助手"
    }
]

while True:
    user_input = input("你: ")
    if user_input == "exit":
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    resp_muti_chat = client.chat.completions.create(
        model = 'deepseek-chat',
        messages = messages,
        temperature = 0.2
    )

    ai_reply = resp_muti_chat.choices[0].message.content

    print("AI:", ai_reply)

    messages.append({
        "role": "assistant",
        "content": ai_reply
    })