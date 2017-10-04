class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        maxNum = 0
        for edge in edges:
            maxNum = max(max(edge[0], edge[1]), maxNum)
        parents = [i for i in range(maxNum+1)]
        for edge in edges:
            parent1, depth1 = self.findParent(parents, edge[0])
            parent2, depth2 = self.findParent(parents, edge[1])
            if parent1 == parent2: return edge
            if depth1 <= depth2:
                parents[parent1] = parent2
            else:
                parents[parent2] = parent1
    
    def findParent(self, parents, i):
        depth = 0
        while i != parents[i]:
            depth += 1
            i = parents[i]
        return i, depth
