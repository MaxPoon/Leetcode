class Solution(object):
	def findRadius(self, houses, heaters):
		"""
		:type houses: List[int]
		:type heaters: List[int]
		:rtype: int
		"""
		radius = 0
		currentHeater = 0
		houses.sort()
		heaters.sort()
		for currentHouse in range(len(houses)):
			while currentHeater < len(heaters) - 1 and abs(heaters[currentHeater] - houses[currentHouse]) >= abs(heaters[currentHeater+1] - houses[currentHouse]): currentHeater+=1
			radius = max(radius, abs(heaters[currentHeater] - houses[currentHouse]))
		return radius