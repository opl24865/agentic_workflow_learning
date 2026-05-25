tool_schemas = [
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "寫入檔案",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string"
                    },
                    "content": {
                        "type": "string"
                    }
                },
                "required": ["filename", "content"]
            }
        }
    },

    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "讀取檔案",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string"
                    }
                },
                "required": ["filename"]
            }
        }
    },
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
        "name": "web_search",
        "description": "搜尋網路資料，取得外部知識",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "要搜尋的關鍵字"
                }
                },
            "required": ["query"]
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "summarize_text",
        "description": "將一段文字整理成摘要",
        "parameters": {
            "type": "object",
            "properties": {
                "text": {
                    "type": "string",
                    "description": "需要摘要的文字"
                },
                "max_length": {
                    "type": "integer",
                    "description": "摘要最大長度，預設 300 字"
                }
                },
            "required": ["text"]
            }
        }
    },
    {
    "type": "function",
    "function": {
        "name": "save_report",
        "description": "將內容儲存成一份報告檔案",
        "parameters": {
            "type": "object",
            "properties": {
                "filename": {
                    "type": "string",
                    "description": "報告檔名，例如 report.txt"
                },
                "title": {
                    "type": "string",
                    "description": "報告標題"
                },
                "content": {
                    "type": "string",
                    "description": "報告內容"
                }
                },
            "required": ["filename", "title", "content"]
            }
        }
    }
]