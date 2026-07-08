import json

from llm.client import ask_llm


class RepositorySummarizer:

    def build_context(self):

        with open("functions.json", encoding="utf-8") as f:
            functions = json.load(f)

        with open("classes.json", encoding="utf-8") as f:
            classes = json.load(f)

        context = []

        context.append(f"Functions: {len(functions)}")
        context.append(f"Classes: {len(classes)}")

        context.append("\nFunctions:\n")

        for function in functions:

            context.append(
                f"- {function['name']} ({function['file_path']})"
            )

        context.append("\nClasses:\n")

        for cls in classes:

            context.append(
                f"- {cls['name']} ({cls['file_path']})"
            )

        return "\n".join(context)

    def summarize(self):

        system_prompt = """
You are an expert software architect.

Generate a concise repository overview.

Include:

- Purpose
- Main components
- Technologies
- High-level workflow
- Suggestions for improvement
"""

        user_prompt = self.build_context()

        return ask_llm(
            system_prompt,
            user_prompt
        )