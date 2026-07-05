from llm.reasoning_engine import RepoMindAssistant

assistant = RepoMindAssistant()

print("=" * 60)
print("REPOMIND AI ASSISTANT")
print("=" * 60)

while True:

    question = input("\nAsk RepoMind (exit to quit): ")

    if question.lower() == "exit":
        break

    answer = assistant.generate_answer(question)

    print()

    print(answer)