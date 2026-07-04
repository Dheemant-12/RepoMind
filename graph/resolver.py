import json


class CallResolver:

    def __init__(self):

        with open("imports.json", encoding="utf-8") as f:
            self.import_data = json.load(f)

    def get_import_map(self, file_path):

        for item in self.import_data:

            if item["file_path"] == file_path:
                return item["import_map"]

        return {}

    def resolve(self, file_path, call_name):

        import_map = self.get_import_map(file_path)

        if call_name in import_map:
            return import_map[call_name]

        return call_name