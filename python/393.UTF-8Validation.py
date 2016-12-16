class Solution(object):
	def validUtf8(self, data):
		"""
		:type data: List[int]
		:rtype: bool
		"""
		i = 0
		while i<len(data):
			byte = data[i]
			shift = 7
			ones = 0
			while shift>=3:
				bit = byte>>shift & 1
				if bit == 1:
					ones+=1
					shift -= 1
				else:
					break
			if ones>4 or ones==1: return False
			elif ones == 0: i+=1
			else:
				if len(data) - i < ones: return False
				bytes = data[i+1:i+ones]
				i += ones
				for byte in bytes:
					if byte>>6 != 2: return False
		return True