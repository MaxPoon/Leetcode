class Solution(object):
	def shortestDistance(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		if grid is None or len(grid) == 0 or len(grid[0]) == 0: return 0
		rows = len(grid)
		cols = len(grid[0])
		visited = [[0]*cols for _ in range(rows)]
		total = [[0]*cols for _ in range(rows)]
		buildings = []
		for r in range(rows):
			for c in range(cols):
				if grid[r][c] == 1: buildings.append((r,c))
		n = len(buildings)
		i = 0
		while len(buildings)>0:
			building = buildings.pop()
			open_state = [(building[0], building[1],0)]
			visitedByThisBuilding = [[False]*cols for _ in range(rows)]
			visitedByThisBuilding[building[0]][building[1]]=True
			count1 = 1
			while len(open_state)>0:
				row,col,d = open_state.pop(0)
				visited[row][col] += 1
				total[row][col] += d
				for r,c in ((row+1,col),(row-1,col), (row,col+1), (row, col-1)):
					if r>=0 and c>=0 and r<rows and c<cols  and grid[r][c]!=2 and visitedByThisBuilding[r][c]==False:
						visitedByThisBuilding[r][c]=True
						if grid[r][c]==0:
							open_state.append((r,c,d+1))
						else: count1+=1
			if count1!=n:return -1
			i+=1
		result = -1
		for row in range(rows):
			for col in range(cols):
				if grid[row][col]==0 and visited[row][col]==i and (result==-1 or total[row][col]<result):
					result = total[row][col]
		return result