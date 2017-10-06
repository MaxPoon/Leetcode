from collections import deque
class Solution(object):
	def findMinHeightTrees(self, n, edges):
		"""
		:type n: int
		:type edges: List[List[int]]
		:rtype: List[int]
		"""
		edgesLists = [[] for _ in range(n)]
		for edge in edges:
			edgesLists[edge[0]].append(edge[1])
			edgesLists[edge[1]].append(edge[0])
		dist = [0]*n
		queue = deque()
		queue.append((0,0))
		visited = set([0])
		while queue:
			node, d = queue.popleft()
			nextDist = d + 1
			for nextNode in edgesLists[node]:
				if nextNode not in visited:
					visited.add(nextNode)
					dist[nextNode] = nextDist
					queue.append((nextNode, nextDist))
		longest = 0
		longestList = []
		for i, d in enumerate(dist):
			if d > longest:
				longestList = [i]
				longest = d
			elif d == longest:
				longestList.append(i)
		start = longestList[0]
		visited = set([start])
		longest = list(self.dfs(start, edgesLists, visited))
		if len(longest)%2 == 1:
			return [longest[len(longest)//2]]
		else:
			i = len(longest)/2
			return longest[i-1:i+1]
	def dfs(self, node, edgesLists, visited):
		longestSubpath = deque()
		for nextNode in edgesLists[node]:
			if nextNode in visited: continue
			visited.add(nextNode)
			subpath = self.dfs(nextNode, edgesLists, visited)
			if len(longestSubpath) < len(subpath):
				longestSubpath = subpath
		longestSubpath.appendleft(node)
		return longestSubpath
