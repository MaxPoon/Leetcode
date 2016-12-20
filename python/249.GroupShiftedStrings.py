class Solution(object):
	def groupStrings(self, strings):
		"""
		:type strings: List[str]
		:rtype: List[List[str]]
		"""
		hashTable = {}
		for string in strings:
			if len(string)==1: 
				if 0 in hashTable:
					hashTable[0].append(string)
				else:
					hashTable[0] = [string]
			else:
				value = 0
				for i in range(1,len(string)):
					value *= 100
					d = ord(string[i]) - ord(string[i-1])
					if d<0:
						d +=26
					d+=1
					value += d
				if value in hashTable:
					hashTable[value].append(string)
				else:
					hashTable[value] = [string]
		result = []
		for v in hashTable.values():
			result.append(v)
		return result