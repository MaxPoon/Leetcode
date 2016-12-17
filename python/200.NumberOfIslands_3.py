class Solution:
	# @param {boolean[][]} grid a boolean 2D matrix
	# @return {int} an integer
	def numIslands(self, grid):
		# Write your code here
		if grid is None or len(grid)==0 or len(grid[0])==0: return 0
		rows = len(grid)
		cols = len(grid[0])
		visited = [[False for col in range(cols)] for row in range(rows)]
		result = 0
		for r in range(rows):
			for c in range(cols):
				if grid[r][c]=='1' and not visited[r][c]:
					result += 1
					visited[r][c]=True
					open_state = [(r,c)]
					while len(open_state):
						row, col = open_state.pop(0)
						for newR, newC in ((row+1,col),(row-1, col),(row,col+1),(row,col-1)):
							if newR>=0 and newC >= 0 and newR<rows and newC<cols and grid[newR][newC] == '1' and not  visited[newR][newC]:
								visited[newR][newC]=True
								open_state.append((newR,newC))
		return result