from pathlib import Path

WORKSPACE = Path("./workspce")
WORKSPACE.mkdir(exist_ok=True)

def write_file(filename: str, content: str):
    path = WORKSPACE / filename
    path.write_text(content, encoding="utf-8")
    return f"已寫入檔案: {filename}"

def read_file(filename: str):
    path = WORKSPACE / filename
    if not path.exists():
        return f'找不到檔案: {filename}'
    
    return path.read_text(encoding="utf-8")

def list_file():
    return [p.name for p in WORKSPACE.iterdir() if p.is_file()]

def web_search(query: str):
    """
    模擬 Web Search 工具。
    實務上可替換成 Tavily / SerpAPI / Brave Search / Google Search API。
    """
    mock_results = {
        "agentic workflow": (
            "Agentic Workflow 是結合 LLM 規劃能力、工具使用與多步驟執行的工作流程。"
            "它通常包含 Planner、Executor、Tool Calling、Memory 等元件。"
        ),
        "rag": (
            "RAG 是 Retrieval-Augmented Generation，透過外部知識檢索補充 LLM 回答。"
        ),
        "llm": (
            "LLM 是大型語言模型，可用於文字生成、摘要、分類、工具調用與推理任務。"
        )
    }

    for keyword, result in mock_results.items():
        if keyword.lower() in query.lower():
            return result

    return f"搜尋結果：找到與「{query}」相關的模擬資料。"

def summarize_text(text: str, max_length: int = 300):
    """
    將文字整理成較短摘要。
    目前是簡單規則版，之後可改成呼叫 LLM 摘要。
    """
    text = text.strip()

    if len(text) <= max_length:
        return text

    return text[:max_length] + "..."

def save_report(filename: str, title: str, content: str):
    """
    將內容存成報告格式。
    """
    path = WORKSPACE / filename

    report = f"""# {title}

    ## 內容摘要

    {content}
    """

    path.write_text(report, encoding="utf-8")

    return f"報告已儲存：{filename}"


available_tools = {
    "write_file": write_file,
    "read_file": read_file,
    "list_file": list_file,
    "web_search": web_search,
    "summarize_text": summarize_text,
    "save_report": save_report

}