def generateNums(base, i, n, current, high, results):
	s = sum(current)
	if len(current)==n: 
		results.append(s)
		return
	for j in range(i, len(base)+len(current)-n+1):
		if s+base[j]<high:
			generateNums(base, j+1, n, current+[base[j]], high, results)
		else: break
	

class Solution(object):
	def readBinaryWatch(self, num):
		"""
		:type num: int
		:rtype: List[str]
		"""
		hours = [1,2,4,8]
		mins = [1,2,4,8,16,32]
		combinations = []
		for h in range(0, min(4,num)+1):
			if num-h > 6: continue
			hourValues = []
			miniValues = []
			generateNums(hours, 0, h, [], 12, hourValues)
			generateNums(mins, 0, num-h, [], 60, miniValues)
			for hour in hourValues:
				for mini in miniValues:
					h_str = str(hour)
					m_str = str(mini) if mini>=10 else "0"+str(mini)
					combinations.append(h_str+":"+m_str)
		return combinations