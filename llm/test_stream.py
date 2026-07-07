from llm.stream_reasoning import StreamingAssistant

assistant = StreamingAssistant()

print("=" * 60)
print("REPOMIND STREAMING")
print("=" * 60)

question = input("\nAsk RepoMind:\n")

print("\n")

for token in assistant.stream_answer(question):

    print(token, end="", flush=True)

print()