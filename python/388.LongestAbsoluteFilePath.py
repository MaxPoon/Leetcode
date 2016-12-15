class Solution(object):
	def lengthLongestPath(self, input):
		"""
		:type input: str
		:rtype: int
		"""
		input = input+"\n"
		level = {}
		currentLevel = 0
		currentLength = 0
		longest = 0
		i = 0
		foundFile = False
		while i < len(input):
			if input[i] == "\n":
				level[currentLevel] = currentLength
				if foundFile:
					length = currentLevel
					for j in range(currentLevel+1):
						length += level[j]
					longest = max(longest, length)
					foundFile = False
				currentLevel = 0
				currentLength = 0
				i = i + 1
				while input[i:i+1] == '\t':
					i+=1
					currentLevel += 1
			else:
				if input[i] == '.': foundFile = True
				currentLength += 1
				i += 1
		return longest