class GraphNode:

    def __init__(self, node_id, node_type, properties):

        self.id = node_id
        self.type = node_type
        self.properties = properties


class GraphEdge:

    def __init__(self, source, target, relation):

        self.source = source
        self.target = target
        self.relation = relation