from graph.query_engine import GraphQueryEngine


class ImpactAnalyzer:

    def __init__(self, graph):
        self.engine = GraphQueryEngine(graph)

    def analyze(self, function_name):

        function = self.engine.find_function(function_name)

        if function is None:

            return {
                "error": f"{function_name} not found."
            }

        callers = self.engine.get_callers(function_name)

        affected_files = set()

        for caller in callers:

            caller_node = self.engine.find_function(caller)

            if caller_node:

                affected_files.add(
                    caller_node.properties["file_path"]
                )

        risk = "Low"

        if len(callers) >= 3:
            risk = "High"

        elif len(callers) > 0:
            risk = "Medium"

        return {

            "function": function_name,

            "direct_callers": callers,

            "affected_files": sorted(list(affected_files)),

            "risk": risk
        }