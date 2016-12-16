class Solution(object):
	def maxKilledEnemies(self, grid):
		"""
		:type grid: List[List[str]]
		:rtype: int
		"""
		if grid is None or len(grid)==0 or len(grid[0]) == 0: return 0
		rows = len(grid)
		cols = len(grid[0])
		left = [[0]*cols for _ in range(rows)]
		right = [[0]*cols for _ in range(rows)]
		up = [[0]*cols for _ in range(rows)]
		down = [[0]*cols for _ in range(rows)]
		currentMax = 0
		for row in range(rows):
			current = 0
			for col in range(cols):
				if grid[row][col] == 'W': current = 0
				left[row][col] = current
				if grid[row][col] == 'E': current+=1
		for row in range(rows):
			current = 0
			for col in range(cols-1, -1, -1):
				if grid[row][col] == 'W': current = 0
				right[row][col] = current
				if grid[row][col] == 'E': current+=1
		for col in range(cols):
			current = 0
			for row in range(rows):
				if grid[row][col] == 'W': current = 0
				up[row][col] = current
				if grid[row][col] == 'E': current+=1
		for col in range(cols):
			current = 0
			for row in range(rows-1, -1, -1):
				if grid[row][col] == 'W': current = 0
				down[row][col] = current
				if grid[row][col] == 'E': current+=1
		for row in range(rows):
			for col in range(cols):
				if grid[row][col]=='W' or grid[row][col] == 'E': continue
				temp = left[row][col] + right[row][col] + up[row][col] + down[row][col] 
				currentMax = max(currentMax, temp)
		return currentMax