from graph.graph_builder import build_graph
from graph.relationship_builder import add_relationships

graph = build_graph()

graph = add_relationships(graph)

print("=" * 60)
print("RESOLVED GRAPH")
print("=" * 60)

print(f"\nNodes : {len(graph.nodes)}")
print(f"Edges : {len(graph.edges)}")

print("\nResolved CALLS Edges:\n")

count = 0

for edge in graph.edges:

    if edge.relation == "CALLS":

        print(
            f"{edge.source}  --->  {edge.target}"
        )

        count += 1

        if count == 20:
            break

graph.save()

print("\n✅ graph.json updated")