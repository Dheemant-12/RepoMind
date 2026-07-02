from graph.graph_builder import build_graph


graph = build_graph()

print("=" * 40)

print(f"Nodes : {len(graph.nodes)}")
print(f"Edges : {len(graph.edges)}")

graph.save()

print("✅ graph.json generated")