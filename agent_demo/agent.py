import json
from planners.task_planner import make_plan
from executors.task_executor import execute_plan

class SimpleAgent:
    def __init__(self, adapter, tools, tool_schemas,system_prompt: str, max_steps: int = 5):
        self.adapter = adapter
        self.tools = tools
        self.tool_schemas = tool_schemas
        self.system_prompt = system_prompt
        self.max_steps = max_steps

    def run(self, user_input: str) -> str:
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": user_input}
        ]

        for step in range(self.max_steps):
            rsp = self.adapter.chat(
                messages,
                tools=self.tool_schemas
            )

            message = rsp["message"]
            messages.append(message)

            print(f"\n--- Step {step + 1} LLM 回覆 ---")
            if message.get("content"):
                print(message["content"])

            tool_calls = message.get("tool_calls") or []

            if tool_calls:
                print("Tool calls:")
                for tc in tool_calls:
                    print("-", tc["function"]["name"])
                    
            if not tool_calls:
                return message.get("content", "")

            for tool_call in tool_calls:
                tool_name = tool_call["function"]["name"]
                args = json.loads(tool_call["function"]["arguments"])

                if tool_name not in self.tools:
                    return f"未知工具: {tool_name}"

                result = self.tools[tool_name](**args)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call["id"],
                    "content": str(result)
                })

        return "超過最大步數，Agent 停止。"



class WorkflowAgent:
    def __init__(self, adapter, base_agent):
        self.adapter = adapter
        self.base_agent = base_agent

    
    def run(self, user_input):
        print("\n=== Planning ===")

        plan = make_plan(
            self.adapter,
            user_input
        )
        print(plan)
        steps = plan["steps"]
        for idx, step in enumerate(steps):
            print(f"{idx+1}. {step}")
        
        print("\n=== Executing ===")

        results = execute_plan(
            self.base_agent,
            steps
        )

        return {
            "plan": steps,
            "results": results
        }