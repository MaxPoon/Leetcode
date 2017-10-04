# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def __init__(self):
        self.memo = {}
    def cloneGraph(self, node):
        if not node: return None
        clonedNode = UndirectedGraphNode(node.label)
        self.memo[clonedNode.label] = clonedNode
        for neighbor in node.neighbors:
            if neighbor.label in self.memo:
                clonedNode.neighbors.append(self.memo[neighbor.label])
            else:
                newNode = self.cloneGraph(neighbor)
                self.memo[newNode.label] = newNode
                clonedNode.neighbors.append(newNode)
        return clonedNode
