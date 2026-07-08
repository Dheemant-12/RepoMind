import json
from collections import defaultdict


class CodebaseHealthAnalyzer:

    def analyze(self):

        with open("functions.json", encoding="utf-8") as f:
            functions = json.load(f)

        with open("classes.json", encoding="utf-8") as f:
            classes = json.load(f)

        files = defaultdict(int)

        for function in functions:
            files[function["file_path"]] += 1

        total_functions = len(functions)
        total_classes = len(classes)
        total_files = len(files)

        average_functions = (
            total_functions / total_files
            if total_files
            else 0
        )

        if total_functions < 20:
            complexity = "Small"

        elif total_functions < 100:
            complexity = "Medium"

        else:
            complexity = "Large"

        suggestions = []

        if total_classes == 0:
            suggestions.append(
                "Repository currently contains no Python classes."
            )

        if average_functions > 10:
            suggestions.append(
                "Some files may contain too many functions."
            )

        if not suggestions:
            suggestions.append(
                "Repository structure looks healthy."
            )

        return {

            "functions": total_functions,

            "classes": total_classes,

            "files": total_files,

            "average_functions_per_file": round(
                average_functions,
                2
            ),

            "complexity": complexity,

            "suggestions": suggestions
        }