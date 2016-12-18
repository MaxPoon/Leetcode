def generate(prefix, word, p, abbrs):
	if p==len(word):
		abbrs.append(prefix)
		return
	generate(prefix+word[p], word, p+1, abbrs)
	for i in range(1,len(word)-p):
		generate(prefix+str(i)+word[p+i],word, p+i+1, abbrs)
	generate(prefix+str(len(word)-p), word, len(word), abbrs)

class Solution(object):
	def generateAbbreviations(self, word):
		"""
		:type word: str
		:rtype: List[str]
		"""
		abbrs = []
		generate("", word, 0, abbrs)
		return abbrs