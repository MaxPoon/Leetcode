class Solution(object):
	def isConvex(self, points):
		"""
		:type points: List[List[int]]
		:rtype: bool
		"""
		def crossProduct(a,b,c):
			return (b[0]-a[0])*(c[1]-a[1]) - (b[1]-a[1])*(c[0]-a[0])
		d = None
		points.append(points[0])
		points.append(points[1])
		for i in range(len(points)):
			a = crossProduct(points[i-2],points[i-1],points[i])
			if a == 0: continue
			if d is None: d = a
			else:
				if a*d < 0: return False
		return True
