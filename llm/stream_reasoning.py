from llm.client import stream_llm
from llm.context_builder import ContextBuilder
from vector.retrieval_engine import RetrievalEngine


class StreamingAssistant:

    def __init__(self):

        self.retriever = RetrievalEngine()

    def stream_answer(self, question):

        context = self.retriever.retrieve(question)

        prompt = ContextBuilder.build(
            question,
            context
        )

        system_prompt = """
You are RepoMind.

Answer only from the supplied repository context.

Be concise and accurate.
"""

        return stream_llm(
            system_prompt,
            prompt
        )