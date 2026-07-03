from graph.query_engine import GraphQueryEngine
from graph.traversal import GraphTraversal


class ImpactAnalyzer:

    def __init__(self, graph):

        self.engine = GraphQueryEngine(graph)
        self.traversal = GraphTraversal(self.engine)

    def analyze(self, function_name):

        function = self.engine.find_function(function_name)

        if function is None:

            return {
                "error": f"{function_name} not found."
            }

        direct_callers = self.engine.get_callers(function_name)

        all_callers = self.traversal.find_all_callers(function_name)

        affected_files = set()

        for caller in all_callers:

            node = self.engine.find_function(caller)

            if node:

                affected_files.add(
                    node.properties["file_path"]
                )

        if len(all_callers) >= 5:
            risk = "High"

        elif len(all_callers) >= 2:
            risk = "Medium"

        else:
            risk = "Low"

        return {

            "function": function_name,

            "direct_callers": direct_callers,

            "all_impacted_functions": all_callers,

            "affected_files": sorted(list(affected_files)),

            "risk": risk
        }