from openai import OpenAI
import os
import json
from pathlib import Path

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

WORKSPACE = Path("./workspace")
WORKSPACE.mkdir(exist_ok=True)

def list_file():
    return [p.name for p in WORKSPACE.iterdir() if p.is_file()]

def create_file(filename: str, content:str):
    path = WORKSPACE / filename
    path.write_text(content, encoding="utf-8")
    return f'已建立檔案:{filename}'

def read_file(filename: str):
    path = WORKSPACE / filename
    if not path.exists():
        return f'找不到檔案:{filename}'
    return path.read_text(encoding="utf-8")

def delete_file(filename: str):
    path = WORKSPACE / filename
    if not path.exists():
        return f"找不到檔案：{filename}"
    path.unlink()
    return f"已刪除檔案：{filename}"


tools = [
    {
        "type": "function",
        "function": {
            "name": "list_file",
            "description": "列出 workspace 內的所有檔案",
            "parameters":{
                "type": "object",
                "properties": {},
                "required": []
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "create_file",
            "description": "在 workspace 內建立文字檔",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string"},
                    "content": {"type": "string"}
                },
                "required": ["filename", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "讀取 workspace 內的文字檔內容",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {"type": "string"}
                },
                "required": ["filename"]
            }
        }
    },
    {
        "type": "function",
        "function":{
            "name": "delete_file",
            "description": "刪除 workspace 內的指定檔案",
            "parameters":{
                "type": "object",
                "properties":{
                    "filename":{"type":"string"}
                },
                "required": ["filename"]
            }
        }
    }
]


messages = [
    {
        "role": "system",
        "content": "你是一個檔案管理助手。需要操作檔案時，請使用工具。"
    },
    {
        "role": "user",
        "content": "幫我建立一個 notes.txt，內容是今天練習 DeepSeek tool calling"
    },
]

available_tools = {
        "list_file": list_file,
        "create_file": create_file,
        "read_file": read_file,
        "delete_file": delete_file
    }

while True:
    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    msg = resp.choices[0].message
    messages.append(msg)

    if not msg.tool_calls:
        print(msg.content)
        break
    
    for tool_call in msg.tool_calls:
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        print("模型選擇工具：", tool_name)
        print("工具參數：", args)

        result = available_tools[tool_name](**args)

        print("工具執行結果：", result)

        messages.append({
            "role": "tool",
            "tool_call_id": tool_call.id,
            "content": json.dumps(result, ensure_ascii=False)
        })

    # if msg.tool_calls:
    #     for tool_call in msg.tool_calls:
    #         tool_name = tool_call.function.name
    #         args = json.loads(tool_call.function.arguments)

    #         print("模型選擇工具：", tool_name)
    #         print("工具參數：", args)
    #         result = available_tools[tool_name](**args)

    #         print("工具執行結果：", result)
    # else:
    #     print(msg.content)
