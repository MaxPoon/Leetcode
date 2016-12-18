class Solution(object):
	def isRectangleCover(self, rectangles):
		"""
		:type rectangles: List[List[int]]
		:rtype: bool
		"""
		bottomLeft = (rectangles[0][0], rectangles[0][1])
		topRight = (rectangles[0][2], rectangles[0][3])
		area = 0
		count = {}
		for rectangle in rectangles:
			point1 = (rectangle[0], rectangle[1])
			point2 = (rectangle[2], rectangle[3])
			point3 = (rectangle[0], rectangle[3])
			point4 = (rectangle[2], rectangle[1])
			if rectangle[0]<=bottomLeft[0] and rectangle[1]<=bottomLeft[1]:
				bottomLeft = point1
			if rectangle[2]>=topRight[0] and rectangle[3]>=topRight[1]:
				topRight = point2
			area += (rectangle[2]-rectangle[0]) * (rectangle[3]-rectangle[1])
			if point1 not in count: count[point1] = 1
			else: count[point1] += 1
			if point2 not in count: count[point2] = 1
			else: count[point2] += 1
			if point3 not in count: count[point3] = 1
			else: count[point3] += 1
			if point4 not in count: count[point4] = 1
			else: count[point4] += 1
		if (topRight[0]-bottomLeft[0])*(topRight[1]-bottomLeft[1])!= area: return False
		topLeft = (bottomLeft[0], topRight[1])
		bottomRight = (topRight[0], bottomLeft[1])
		for point, v in count.iteritems():
			if (point==bottomLeft or point==topRight or point==bottomRight or point==topLeft) and v!=1: return False
			if point!=bottomLeft and point!=topRight and point!=bottomRight and point!=topLeft and v&1==1:return False 
		return True