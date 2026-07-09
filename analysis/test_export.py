from analysis.graph_export import GraphExporter

exporter = GraphExporter()

path = exporter.export()

print("=" * 60)
print("GRAPH EXPORT")
print("=" * 60)

print(f"Exported graph to: {path}")