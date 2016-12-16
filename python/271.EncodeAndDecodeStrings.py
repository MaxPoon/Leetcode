class Codec:

	def encode(self, strs):
		"""Encodes a list of strings to a single string.
		
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs) == 0: return ""
		t = ""
		for s in strs:
			newS = s.replace('0101010', '01010100')
			t += newS + '#01010101'
		return t

	def decode(self, s):
		"""Decodes a single string to a list of strings.
		
		:type s: str
		:rtype: List[str]
		"""
		if s == "": return []
		strs = []
		i = s.find('01010101')
		while i!=-1:
			newS = s[:i-1]
			newS = newS.replace('01010100', '0101010')
			strs.append(newS)
			s = s[i+8:]
			i = s.find('01010101')
		return strs
		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))