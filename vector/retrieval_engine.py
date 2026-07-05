from vector.query_router import classify_query
from vector.semantic_search import semantic_search

from graph.graph_builder import build_graph
from graph.relationship_builder import add_relationships
from graph.impact_analyzer import ImpactAnalyzer


class RetrievalEngine:

    def __init__(self):

        self.graph = build_graph()
        self.graph = add_relationships(self.graph)

        self.analyzer = ImpactAnalyzer(self.graph)

    def retrieve(self, question):

        route = classify_query(question)

        if route == "SEMANTIC":

            return {

                "route": "SEMANTIC",

                "results": semantic_search(question)
            }

        elif route == "GRAPH":

            function = question.split()[-1]

            return {

                "route": "GRAPH",

                "results": self.analyzer.analyze(function)
            }

        else:

            function = question.split()[-1]

            return {

                "route": "HYBRID",

                "semantic": semantic_search(question),

                "graph": self.analyzer.analyze(function)
            }