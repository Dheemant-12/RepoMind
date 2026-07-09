import json
import os

from graph.graph_builder import build_graph
from graph.relationship_builder import add_relationships


class GraphExporter:

    def export(self, filename="graph_export.json"):

        graph = build_graph()
        graph = add_relationships(graph)

        export_data = {

            "summary": {

                "nodes": len(graph.nodes),

                "edges": len(graph.edges)

            },

            "nodes": [],

            "edges": []

        }

        for node in graph.nodes:

            export_data["nodes"].append({

                "id": node.id,

                "type": node.type,

                "properties": node.properties

            })

        for edge in graph.edges:

            export_data["edges"].append({

                "source": edge.source,

                "target": edge.target,

                "relation": edge.relation

            })

        os.makedirs("exports", exist_ok=True)

        output_path = os.path.join("exports", filename)

        with open(output_path, "w", encoding="utf-8") as f:

            json.dump(export_data, f, indent=4)

        return output_path