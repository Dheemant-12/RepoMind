from graph.graph_builder import build_graph
from graph.relationship_builder import add_relationships
from graph.impact_analyzer import ImpactAnalyzer

graph = build_graph()

graph = add_relationships(graph)

analyzer = ImpactAnalyzer(graph)

result = analyzer.analyze("clone_repository")

print("=" * 50)

print("IMPACT ANALYSIS")

print("=" * 50)

print()

for key, value in result.items():

    print(f"{key}: {value}")