class Solution(object):
	def longestLine(self, M):
		"""
		:type M: List[List[int]]
		:rtype: int
		"""
		if len(M) < 1 or len(M[0]) < 1: return 0
		rows = len(M)
		cols = len(M[0])
		longest = 0
		directions = ((1, 0), (0, 1), (1, 1), (1, -1))
		visited = [[[False]*4 for col in range(cols)] for row in range(rows)]
		for row in range(rows):
			for col in range(cols):
				if M[row][col] != 1: continue
				for direction in range(4):
					if visited[row][col][direction]: continue
					dy, dx = directions[direction]
					currentLen = 1
					y, x = row, col
					while True:
						visited[y][x][direction] = True
						y, x = y+dy, x+dx
						if 0<=y<rows and 0<=x<cols and M[y][x]==1:
							currentLen += 1
						else:
							break
					longest = max(longest, currentLen)
		return longest
