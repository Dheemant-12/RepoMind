import json
from collections import Counter


class RepositoryMetrics:

    def calculate(self):

        with open("functions.json", encoding="utf-8") as f:
            functions = json.load(f)

        with open("classes.json", encoding="utf-8") as f:
            classes = json.load(f)

        with open("imports.json", encoding="utf-8") as f:
            imports = json.load(f)

        metrics = {}

        metrics["total_functions"] = len(functions)
        metrics["total_classes"] = len(classes)
        metrics["total_files"] = len(imports)

        file_counter = Counter()

        for function in functions:
            file_counter[function["file_path"]] += 1

        metrics["top_files"] = file_counter.most_common(5)

        total_imports = 0

        for item in imports:
            total_imports += len(item["imports"])

        metrics["total_imports"] = total_imports

        if metrics["total_files"] > 0:
            metrics["average_functions_per_file"] = round(
                metrics["total_functions"] / metrics["total_files"],
                2
            )
        else:
            metrics["average_functions_per_file"] = 0

        return metrics