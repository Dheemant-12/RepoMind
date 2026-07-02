import json

from graph.graph_models import GraphNode, GraphEdge


class RepoGraph:

    def __init__(self):

        self.nodes = []
        self.edges = []

    def add_node(self, node):

        self.nodes.append(node)

    def add_edge(self, edge):

        self.edges.append(edge)

    def save(self, filename="graph.json"):

        data = {

            "nodes": [
                {
                    "id": n.id,
                    "type": n.type,
                    "properties": n.properties
                }
                for n in self.nodes
            ],

            "edges": [
                {
                    "source": e.source,
                    "target": e.target,
                    "relation": e.relation
                }
                for e in self.edges
            ]
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)


def build_graph():

    graph = RepoGraph()

    with open("functions.json", encoding="utf-8") as f:
        functions = json.load(f)

    with open("classes.json", encoding="utf-8") as f:
        classes = json.load(f)

    for function in functions:

        graph.add_node(
            GraphNode(
                function["name"],
                "Function",
                function
            )
        )

    for cls in classes:

        graph.add_node(
            GraphNode(
                cls["name"],
                "Class",
                cls
            )
        )

    return graph