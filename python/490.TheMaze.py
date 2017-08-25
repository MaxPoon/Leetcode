class Solution(object):
	def hasPath(self, maze, start, destination):
		"""
		:type maze: List[List[int]]
		:type start: List[int]
		:type destination: List[int]
		:rtype: bool
		"""
		start = tuple(start)
		destination = tuple(destination)
		if start == destination:
			return True
		directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
		width = len(maze)
		height = len(maze[0])
		if 1 <= destination[0] < width-1 and 1 <= destination[1] < height-1:
			if not any([maze[destination[0]+direction[0]][destination[1]+direction[1]] for direction in directions]):
				return False
		positions = [start]
		visited = set()
		while positions:
			position = positions.pop(0)
			for direction in directions:
				if (position + direction) in visited: continue
				nextPosition = position
				while (nextPosition+direction) not in visited:
					visited.add(nextPosition+direction)
					prevPosition = nextPosition
					nextPosition = (nextPosition[0]+direction[0], nextPosition[1]+direction[1])
					if not 0 <= nextPosition[0] < width or not 0 <= nextPosition[1] < height or maze[nextPosition[0]][nextPosition[1]] == 1:
						if prevPosition == destination:
							return True
						positions.append(prevPosition)
						break
		return False
