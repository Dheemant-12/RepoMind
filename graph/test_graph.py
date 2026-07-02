from graph.graph_builder import build_graph
from graph.relationship_builder import add_relationships

graph = build_graph()

graph = add_relationships(graph)

print("=" * 40)

print(f"Nodes : {len(graph.nodes)}")
print(f"Edges : {len(graph.edges)}")

graph.save()

print("\nSample Relationships:\n")

for edge in graph.edges[:10]:
    print(
        edge.source,
        "--",
        edge.relation,
        "-->",
        edge.target
    )

print("\n✅ graph.json updated")