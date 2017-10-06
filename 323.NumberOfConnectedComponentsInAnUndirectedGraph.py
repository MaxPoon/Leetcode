class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        edgesLists = [[] for _ in range(n)]
        for edge in edges:
            edgesLists[edge[0]].append(edge[1])
            edgesLists[edge[1]].append(edge[0])
        visited = set()
        count = 0
        for start in range(n):
            if start in visited: continue
            count += 1
            stack = [start]
            visited.add(start)
            while stack:
                node = stack.pop()
                for nextNode in edgesLists[node]:
                    if nextNode not in visited:
                        visited.add(nextNode)
                        stack.append(nextNode)
        return count
