class GraphTraversal:

    def __init__(self, engine):
        self.engine = engine

    def find_all_callers(self, function_name):

        visited = set()
        result = []

        def dfs(current):

            callers = self.engine.get_callers(current)

            for caller in callers:

                if caller not in visited:

                    visited.add(caller)
                    result.append(caller)

                    dfs(caller)

        dfs(function_name)

        return result