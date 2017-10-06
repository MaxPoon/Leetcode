from collections import Counter
class Solution(object):
	def removeDuplicateLetters(self, s):
		"""
		:type s: str
		:rtype: str
		"""
		charsSet = set(s)
		result = []
		current = 0
		added = set()
		while len(result)<len(charsSet):
			pos = current
			minC = 'z'
			counter = Counter(s[current:])
			for i in range(current, len(s)):
				c = s[i]
				if c in added: continue
				if c < minC:
					pos = i
					minC = c
				counter[c] -= 1
				if counter[c] == 0:
					result.append(minC)
					current = pos+1
					added.add(minC)
					break
		return ''.join(result)
