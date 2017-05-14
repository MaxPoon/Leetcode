class Solution(object):
	def isReflected(self, points):
		"""
		:type points: List[List[int]]
		:rtype: bool
		"""
		if not points: return True
		left = min(points)[0]
		right = max(points)[0]
		x = (left+right)/2.0
		pointsSet = set()
		for point in points:
			pointsSet.add(tuple(point))
		for point in points:
			reflected = (2*x-point[0], point[1])
			if reflected not in pointsSet:
				return False
		return True