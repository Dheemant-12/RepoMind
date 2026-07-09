import json
import os
from collections import Counter


class RepositoryReport:

    def generate(self):

        with open("functions.json", encoding="utf-8") as f:
            functions = json.load(f)

        with open("classes.json", encoding="utf-8") as f:
            classes = json.load(f)

        with open("imports.json", encoding="utf-8") as f:
            imports = json.load(f)

        file_counter = Counter()

        for function in functions:
            file_counter[function["file_path"]] += 1

        report = {

            "summary": {

                "total_functions": len(functions),

                "total_classes": len(classes),

                "total_python_files": len(imports),

                "total_imports": sum(
                    len(item["imports"])
                    for item in imports
                )

            },

            "top_files": [

                {
                    "file": file,
                    "functions": count
                }

                for file, count in file_counter.most_common(5)

            ]
        }

        os.makedirs("reports", exist_ok=True)

        output_path = os.path.join(
            "reports",
            "repository_report.json"
        )

        with open(output_path, "w", encoding="utf-8") as f:

            json.dump(
                report,
                f,
                indent=4
            )

        return output_path