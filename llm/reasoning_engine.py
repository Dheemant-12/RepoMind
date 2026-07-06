from llm.memory import ConversationMemory
from vector.retrieval_engine import RetrievalEngine


class RepoMindAssistant:

    def __init__(self):

        self.retriever = RetrievalEngine()
        self.memory = ConversationMemory()

    def build_context(self, question):

        return self.retriever.retrieve(question)

    def generate_answer(self, question):

        # Resolve follow-up questions like "What calls it?"
        question = self.memory.resolve_question(question)

        context = self.build_context(question)

        route = context["route"]

        if route == "SEMANTIC":

            result = context["results"][0]

            self.memory.update(
                question,
                result["source"],
                result["function"]
            )

            return f"""
Question:
{question}

Answer:

The most relevant function is '{result["function"]}'.

Location:
{result["file"]}

This function appears to be the best match based on semantic similarity.

Similarity Distance:
{result["distance"]:.4f}

Summary:

{result["source"][:350]}
"""

        elif route == "GRAPH":

            graph = context["results"]

            self.memory.update(
                question,
                str(graph),
                graph["function"]
            )

            return f"""
Question:
{question}

Impact Analysis

Target Function:
{graph["function"]}

Direct Callers:
{graph["direct_callers"]}

Affected Files:
{graph["affected_files"]}

Estimated Risk:
{graph["risk"]}
"""

        else:

            semantic = context["semantic"][0]
            graph = context["graph"]

            self.memory.update(
                question,
                str(context),
                semantic["function"]
            )

            return f"""
Question:
{question}

Hybrid Analysis

Relevant Function:
{semantic["function"]}

Location:
{semantic["file"]}

Risk:
{graph["risk"]}

Affected Files:
{graph["affected_files"]}

Code Preview:

{semantic["source"][:300]}
"""