class Solution(object):
	def minArea(self, image, x, y):
		"""
		:type image: List[List[str]]
		:type x: int
		:type y: int
		:rtype: int
			"""
		def first(lo, hi, check):
			while lo < hi:
				mid = (lo + hi) / 2
				if check(mid):
					hi = mid
				else:
					lo = mid + 1
			return lo
		top    = first(0, x,             lambda x: '1' in image[x])
		bottom = first(x, len(image),    lambda x: '1' not in image[x])
		left   = first(0, y,             lambda y: any(row[y] == '1' for row in image))
		right  = first(y, len(image[0]), lambda y: all(row[y] == '0' for row in image))
		return (bottom - top) * (right - left)