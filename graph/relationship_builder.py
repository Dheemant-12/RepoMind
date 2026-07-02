import json

from graph.graph_models import GraphEdge


def add_relationships(graph):

    with open("functions.json", encoding="utf-8") as f:
        functions = json.load(f)

    with open("calls.json", encoding="utf-8") as f:
        calls = json.load(f)

    file_nodes = set()

    # ---------- File Nodes + DEFINED_IN ----------

    for function in functions:

        file_path = function["file_path"]

        if file_path not in file_nodes:

            graph.add_node(
                type(
                    graph.nodes[0]
                )(
                    file_path,
                    "File",
                    {
                        "path": file_path
                    }
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

    # ---------- CALLS ----------

    for function in calls:

        caller = function["function"]

        for called in function["calls"]:

            graph.add_edge(
                GraphEdge(
                    caller,
                    called,
                    "CALLS"
                )
            )

    return graph