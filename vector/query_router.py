GRAPH_KEYWORDS = {

    "call",
    "calls",
    "caller",
    "callee",
    "dependency",
    "dependencies",
    "impact",
    "break",
    "affected",
    "inherit",
    "inherits"
}


HYBRID_KEYWORDS = {

    "modify",
    "change",
    "update",
    "refactor",
    "effect",
    "risk"
}


def classify_query(question: str):

    question = question.lower()

    graph_score = 0
    hybrid_score = 0

    for keyword in GRAPH_KEYWORDS:

        if keyword in question:
            graph_score += 1

    for keyword in HYBRID_KEYWORDS:

        if keyword in question:
            hybrid_score += 1

    if hybrid_score > 0:
        return "HYBRID"

    if graph_score > 0:
        return "GRAPH"

    return "SEMANTIC"