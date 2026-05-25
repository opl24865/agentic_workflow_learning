from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from agent import SimpleAgent, WorkflowAgent
from adapters.factory import get_adapter
from prompts.system_prompt import SYSTEM_PROMPT
from tool.tools import available_tools
from tool.schema import tool_schemas

app = FastAPI()




class ChatRequest(BaseModel):
    message: str


adapter = get_adapter("ollama")

base_agent = SimpleAgent(
    adapter=adapter,
    tools=available_tools,
    tool_schemas=tool_schemas,
    system_prompt=SYSTEM_PROMPT,
    max_steps=5
)

workflow_agent = WorkflowAgent(
    adapter=adapter,
    base_agent=base_agent
)


@app.post("/chat")
def chat(req: ChatRequest):
    result = workflow_agent.run(req.message)
    return result

app.mount("/", StaticFiles(directory="static", html=True), name="static")