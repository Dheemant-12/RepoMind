from graph.graph_builder import build_graph
from graph.relationship_builder import add_relationships
from graph.query_engine import GraphQueryEngine

graph = build_graph()

graph = add_relationships(graph)

engine = GraphQueryEngine(graph)

print("=" * 50)
print("REPOMIND QUERY ENGINE")
print("=" * 50)

print("\nFind Function\n")

function = engine.find_function("main")

if function:
    print(function.properties)

print("\nFunctions Called by 'main'\n")

print(engine.get_called_functions("main"))

print("\nWho Calls 'main'\n")

print(engine.get_callers("main"))

print("\nFunctions In Same File\n")

if function:

    file_path = function.properties["file_path"]

    for func in engine.get_functions_in_file(file_path):
        print("-", func.id)

print("\nDone.")