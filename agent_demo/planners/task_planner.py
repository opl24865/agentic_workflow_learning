from email import message
import json

SYSTEM_PROMPT = """
你是一個 Task Planner。

請將使用者需求拆解成步驟。

規則：
1. 一次只做一件事
2. 步驟要清楚
3. 只回傳 JSON

格式：

{
  "steps": [
    "步驟1",
    "步驟2"
  ]
}
"""


def make_plan(adapter, user_input):
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    rsp = adapter.chat(messages)

    try:
        return json.loads(rsp["message"]["content"])
        
    except Exception as e:
        print("Planner JSON 解析失敗：", e)
        return {
            "steps": [user_input]
        }