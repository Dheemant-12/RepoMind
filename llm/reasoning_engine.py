import json

from vector.retrieval_engine import RetrievalEngine


class RepoMindAssistant:

    def __init__(self):

        self.retriever = RetrievalEngine()

    def build_context(self, question):

        return self.retriever.retrieve(question)

    def generate_answer(self, question):

        context = self.build_context(question)

        route = context["route"]

        if route == "SEMANTIC":

            result = context["results"][0]

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

            return f"""
Question:
{question}

Hybrid Analysis

Relevant Function

{semantic["function"]}

Location

{semantic["file"]}

Risk

{graph["risk"]}

Affected Files

{graph["affected_files"]}

Code Preview

{semantic["source"][:300]}
"""