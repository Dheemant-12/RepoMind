from graph.graph_builder import build_graph
from graph.relationship_builder import add_relationships

graph = build_graph()

graph = add_relationships(graph)

graph.save()

print("=" * 50)

print("GRAPH SUMMARY")

print("=" * 50)

print(f"Nodes : {len(graph.nodes)}")
print(f"Edges : {len(graph.edges)}")

print("\nNode Types")

counts = {}

for node in graph.nodes:

    counts[node.type] = counts.get(node.type, 0) + 1

for key, value in counts.items():

    print(f"{key}: {value}")

print("\nLookup Test")

print(graph.get_node("main"))

print("\nGraph generated successfully.")