from agent import SimpleAgent, WorkflowAgent
from adapters.factory import get_adapter
from prompts.system_prompt import SYSTEM_PROMPT
from tool.tools import available_tools
from tool.schema import tool_schemas


def agent_main():
    adapter = get_adapter("Groq")

    agent = SimpleAgent(
        adapter=adapter,
        tools=available_tools,
        tool_schemas=tool_schemas,
        system_prompt=SYSTEM_PROMPT,
        max_steps=5
    )

    while True:
        user_input = input("\n你：")

        if user_input.lower() in ["exit", "quit"]:
            break

        answer = agent.run(user_input)
        print("\nAgent：", answer)

def agentic_main():
    adapter = get_adapter("ollama")

    base_agent = SimpleAgent(
        adapter=adapter,
        tools=available_tools,
        tool_schemas=tool_schemas,
        system_prompt=SYSTEM_PROMPT,
        max_steps=5
    )

    Workflow_agent = WorkflowAgent(
        adapter,
        base_agent
    )

    while True:
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit", "q"]:
            print("Bye!")
            break
        if not user_input:
            continue
        try:
            result = Workflow_agent.run(user_input)
        except Exception as e:
            print(f"\n發生錯誤：{e}")

    # print(result)

if __name__ == "__main__":
    agentic_main()