class Solution(object):
	def maxKilledEnemies(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
class Solution(object):
	def maxKilledEnemies(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		m, n = len(grid), 0
		if m:
			n = len(grid[0])
		result, rows = 0, 0
		cols = [0 for i in range(n)]

		for i in range(m):
			for j in range(n):
				if j == 0 or grid[i][j-1] == 'W':
					rows = 0
					for k in range(j, n):
						if grid[i][k] == 'W':
							break
						if grid[i][k] == 'E':
							rows += 1

				if i == 0 or grid[i-1][j] == 'W':
					cols[j] = 0
					for k in range(i, m):
						if grid[k][j] == 'W':
							break
						if grid[k][j] == 'E':
							cols[j] += 1

				if grid[i][j] == '0' and rows + cols[j] > result:
					result = rows + cols[j]

		return result