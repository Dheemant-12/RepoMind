from llm.client import ask_llm
from llm.context_builder import ContextBuilder
from llm.memory import ConversationMemory
from vector.retrieval_engine import RetrievalEngine


class RepoMindAssistant:

    def __init__(self):

        self.retriever = RetrievalEngine()
        self.memory = ConversationMemory()

    def generate_answer(self, question):

        question = self.memory.resolve_question(question)

        context = self.retriever.retrieve(question)

        prompt = ContextBuilder.build(
            question,
            context
        )

        system_prompt = """
You are RepoMind.

You are an expert software architect.

Answer ONLY from the supplied repository context.

If the context is insufficient, clearly say so.

Keep answers concise and technically accurate.
"""

        answer = ask_llm(
            system_prompt,
            prompt
        )

        function_name = None

        try:

            if context["route"] == "SEMANTIC":
                function_name = context["results"][0]["function"]

            elif context["route"] == "GRAPH":
                function_name = context["results"]["function"]

            elif context["route"] == "HYBRID":
                function_name = context["semantic"][0]["function"]

        except Exception:
            pass

        self.memory.update(
            question,
            answer,
            function_name
        )

        return answer