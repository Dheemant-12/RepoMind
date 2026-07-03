class GraphQueryEngine:

    def __init__(self, graph):
        self.graph = graph

    def find_function(self, function_name):
        node = self.graph.get_node(function_name)

        if node and node.type == "Function":
            return node

        return None

    def get_functions_in_file(self, file_path):

        functions = []

        for edge in self.graph.edges:

            if edge.relation == "DEFINED_IN" and edge.target == file_path:

                node = self.graph.get_node(edge.source)

                if node:
                    functions.append(node)

        return functions

    def get_called_functions(self, function_name):

        calls = []

        for edge in self.graph.edges:

            if edge.relation == "CALLS" and edge.source == function_name:

                calls.append(edge.target)

        return calls

    def get_callers(self, function_name):

        callers = []

        for edge in self.graph.edges:

            if edge.relation == "CALLS" and edge.target == function_name:

                callers.append(edge.source)

        return callers