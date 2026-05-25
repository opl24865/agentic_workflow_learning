def execute_plan(agent, steps):
    results = []
    context = ""

    for idx, step in enumerate(steps):
        print(f"\n[Step {idx+1}] {step}")

        prompt = f"""
                目前工作上下文：

                {context}

                現在請執行：
                {step}
                """

        result = agent.run(prompt)

        results.append({
            "step": step,
            "result": result
        })

        context += f"\n\n[{step}]\n{result}"

    return results