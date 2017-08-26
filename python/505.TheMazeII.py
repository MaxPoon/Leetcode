class Solution(object):
	def shortestDistance(self, maze, start, destination):
		"""
		:type maze: List[List[int]]
		:type start: List[int]
		:type destination: List[int]
		:rtype: int
		"""
		start = tuple(start)
		destination = tuple(destination)
		directions = ((0, 1), (0, -1), (1, 0), (-1, 0))
		positions = [start+direction+(0,) for direction in directions]
		width = len(maze)
		height = len(maze[0])
		visited = set()
		while positions:
			position = positions.pop(0)
			nextDistance = position[-1] + 1
			direction = position[2:4]
			position = position[:2]
			absoluteDirection = (abs(direction[0]), abs(direction[1]))
			nextPosition = (position[0]+direction[0], position[1]+direction[1])
			if not 0 <= nextPosition[0] < width or not 0 <= nextPosition[1] < height or maze[nextPosition[0]][nextPosition[1]] == 1:
				if position == destination: return nextDistance-1
				for otherDirection in directions:
					nextPosition = (position[0]+otherDirection[0], position[1]+otherDirection[1])
					if 0 <= nextPosition[0] < width and 0 <= nextPosition[1] < height and maze[nextPosition[0]][nextPosition[1]] != 1:
						absoluteDirection = (abs(otherDirection[0]), abs(otherDirection[1]))
						if (nextPosition+absoluteDirection) not in visited:
							positions.append(nextPosition+otherDirection+(nextDistance,))
							visited.add(nextPosition+absoluteDirection)
				visited.add(nextPosition+absoluteDirection)
			elif (nextPosition+absoluteDirection) not in visited:
				positions.append(nextPosition+direction+(nextDistance,))
				visited.add(nextPosition+absoluteDirection)
		return -1
