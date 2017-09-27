class Solution(object):
	def findLonelyPixel(self, picture):
		"""
		:type picture: List[List[str]]
		:rtype: int
		"""
		uniqueInRow = set()
		if not picture or not picture[0]: return 0
		for i, row in enumerate(picture):
			position = None
			for j, pixel in enumerate(row):
				if pixel == 'W': continue
				if position:
					position = None
					break
				position = (i,j)
			if position:
				uniqueInRow.add(position)
		count = 0
		for j in range(len(picture[0])):
			position = None
			for i in range(len(picture)):
				pixel = picture[i][j]
				if pixel == 'W': continue
				if position:
					position = None
					break
				position = (i,j)
			if position and position in uniqueInRow:
				count += 1
		return count
