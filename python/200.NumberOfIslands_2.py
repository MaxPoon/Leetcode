def findParentDepth(isLands, point):
	depth = 0 
	while point != isLands[point[0]][point[1]] and isLands[point[0]][point[1]] != isLands[isLands[point[0]][point[1]][0]][isLands[point[0]][point[1]][1]]:
		isLands[point[0]][point[1]] = isLands[isLands[point[0]][point[1]][0]][isLands[point[0]][point[1]][1]]
		depth += 1
	if point != isLands[point[0]][point[1]]:
		point = isLands[point[0]][point[1]]
		depth += 1
	return (point, depth)

def connect(isLands, point1, point2):
	parent1, depth1 = findParentDepth(isLands,point1)
	parent2, depth2 = findParentDepth(isLands,point2)
	if depth2<= depth1:
		isLands[parent2[0]][parent2[1]] = parent1
	else:
		isLands[parent1[0]][parent1[1]] = parent2

class Solution:
	# @param {boolean[][]} grid a boolean 2D matrix
	# @return {int} an integer
	def numIslands(self, grid):
		# Write your code here
		if grid is None or len(grid)==0 or len(grid[0])==0: return 0
		rows = len(grid)
		cols = len(grid[0])
		isLands = [[(row, col) for col in range(cols)] for row in range(rows)]
		for r in range(rows):
			for c in range(cols):
				if grid[r][c]=='1':
					if r+1<rows and grid[r+1][c]=='1': connect(isLands, (r,c), (r+1,c))
					if c+1 < cols and grid[r][c+1]=='1': connect(isLands, (r,c), (r,c+1))
		isLandsSet = set()
		for r in range(rows):
			for c in range(cols):
				if grid[r][c]=='1':
					isLandsSet.add(findParentDepth(isLands,(r,c))[0])
		return len(isLandsSet)