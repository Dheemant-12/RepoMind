from llm.memory import ConversationMemory
from llm.client import ask_llm
from vector.retrieval_engine import RetrievalEngine


class RepoMindAssistant:

    def __init__(self):

        self.retriever = RetrievalEngine()
        self.memory = ConversationMemory()

    def build_context(self, question):

        return self.retriever.retrieve(question)

    def generate_answer(self, question):

        # Resolve follow-up questions
        question = self.memory.resolve_question(question)

        # Retrieve repository context
        context = self.build_context(question)

        # System prompt
        system_prompt = """
You are RepoMind, an AI Software Architect.

You answer questions about source code repositories.

Use ONLY the repository context provided.

If the answer cannot be determined from the context,
say that the repository does not contain enough information.

Be concise, accurate, and professional.
"""

        # User prompt
        user_prompt = f"""
User Question:

{question}

Repository Context:

{context}

Generate a helpful answer for the developer.
"""

        # Get AI response
        answer = ask_llm(
            system_prompt=system_prompt,
            user_prompt=user_prompt
        )

        # Store memory
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
            question=question,
            answer=answer,
            function_name=function_name
        )

        return answer