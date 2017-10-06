class Solution(object):
	def validTree(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: bool
		"""
		if len(edges) != n-1: return False
		edgesLists = [[] for _ in range(n)]
		for edge in edges:
			edgesLists[edge[0]].append(edge[1])
			edgesLists[edge[1]].append(edge[0])
		stack = [0]
		visited = set(stack)
		while stack:
			node = stack.pop()
			for nextNode in edgesLists[node]:
				if nextNode not in visited:
					visited.add(nextNode)
					stack.append(nextNode)
		return len(visited) == n
