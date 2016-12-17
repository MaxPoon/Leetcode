def findParentDepth(isLands, point):
	depth = 0 
	while point != isLands[point] and isLands[point] != isLands[isLands[point]]:
		isLands[point] = isLands[isLands[point]]
		depth += 1
	if point != isLands[point]:
		point = isLands[point]
		depth += 1
	return (point, depth)

def connect(isLands, point1, point2):
	parent1, depth1 = findParentDepth(isLands,point1)
	parent2, depth2 = findParentDepth(isLands,point2)
	if depth2<= depth1:
		isLands[parent2] = parent1
	else:
		isLands[parent1] = parent2

class Solution(object):
	def numIslands2(self, m, n, positions):
		"""
		:type m: int
		:type n: int
		:type positions: List[List[int]]
		:rtype: List[int]
		"""
		lands = set()
		numOfIslands = 0
		isLands = {}
		result = []
		for i in range(len(positions)):
			position = tuple(positions[i])
			isLands[position] = position
			r, c = position
			lands.add(tuple(position))
			merge = set()
			for row, col in ((r+1, c), (r-1,c),(r,c+1), (r,c-1)):
				if (row,col) in isLands:
					merge.add(findParentDepth(isLands,(row,col))[0])
			if len(merge) == 0:
				numOfIslands += 1
				result.append(numOfIslands)
			else:
				numOfIslands = numOfIslands + 1 - len(merge)
				result.append(numOfIslands)
				merge = [position] + list(merge)
				for i in range(len(merge)-1):
					connect(isLands, merge[i], merge[i+1])
		return result