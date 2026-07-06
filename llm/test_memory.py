from llm.reasoning_engine import RepoMindAssistant

assistant = RepoMindAssistant()

print("=" * 60)
print("REPOMIND CHAT")
print("=" * 60)

while True:

    question = input("\nYou: ")

    if question.lower() == "exit":
        break

    if question.lower() == "clear":

        assistant.memory.clear()

        print("Conversation cleared.")

        continue

    answer = assistant.generate_answer(question)

    print()

    print(answer)