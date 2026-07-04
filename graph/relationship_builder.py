import json

from graph.graph_models import GraphEdge, GraphNode
from graph.resolver import CallResolver


def add_relationships(graph):

    resolver = CallResolver()

    with open("functions.json", encoding="utf-8") as f:
        functions = json.load(f)

    with open("calls.json", encoding="utf-8") as f:
        calls = json.load(f)

    file_nodes = set()

    # File Nodes
    for function in functions:

        file_path = function["file_path"]

        if file_path not in file_nodes:

            graph.add_node(
                GraphNode(
                    file_path,
                    "File",
                    {"path": file_path}
                )
            )

            file_nodes.add(file_path)

        graph.add_edge(
            GraphEdge(
                function["name"],
                file_path,
                "DEFINED_IN"
            )
        )

    # CALLS (Resolved)
    for function in calls:

        caller = function["function"]

        for raw_call in function["calls"]:

            resolved = resolver.resolve(
                function["file_path"],
                raw_call
            )

            graph.add_edge(
                GraphEdge(
                    caller,
                    resolved,
                    "CALLS"
                )
            )

    return graph