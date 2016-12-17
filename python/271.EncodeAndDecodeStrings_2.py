class Codec:
	def encode(self, strs):
		"""Encodes a list of strings to a single string.
		
		:type strs: List[str]
		:rtype: str
		"""
		if len(strs) == 0: return ""
		t = ""
		for s in strs:
			l = len(s)
			t += str(l)+'#'+s
		return t

	def decode(self, s):
		"""Decodes a single string to a list of strings.
		
		:type s: str
		:rtype: List[str]
		"""
		if s == "": return []
		strs = []
		i = 0
		l = ""
		while i<len(s):
			if s[i]=='#':
				l = int(l)
				newS = s[i+1: i+1+l]
				strs.append(newS)
				i = i+1+l
				l=""
			else:
				l+=s[i]
				i+=1
		return strs
		

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))