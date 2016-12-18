def generate(prefix, word, p, abbrs):
	if p==len(word):
		abbrs.append(prefix)
		return
	generate(prefix+word[p], word, p+1, abbrs)
	for i in range(2,len(word)-p):
		generate(prefix+str(i)+word[p+i],word, p+i+1, abbrs)
	generate(prefix+str(len(word)-p), word, len(word), abbrs)
	
def validWordAbbreviation(word, abbr):
	p1 = 0
	p2 = 0
	while p1<len(word) and p2<len(abbr):
		if abbr[p2].isdigit():
			if int(abbr[p2])==0: return False
			i = 0
			while p2+i<len(abbr) and abbr[p2+i].isdigit():
				i+=1
			n = int(abbr[p2:p2+i])
			if len(word)-p1<n: return False
			else: 
				p1+=n
				p2+=i
		else:
			if abbr[p2]!=word[p1]: return False
			else:
				p1+=1
				p2+=1
	if p1!=len(word) or p2!=len(abbr): return False
	return True

class Solution(object):
	def minAbbreviation(self, target, dictionary):
		"""
		:type target: str
		:type dictionary: List[str]
		:rtype: str
		"""
		dictionary = [word for word in dictionary if len(word)==len(target)]
		if len(dictionary)==0:
			return str(len(target))
		abbrs = []
		generate("", target, 0, abbrs)
		minLength = len(target)
		minAbbr = target
		for abbr in abbrs:
			length = 0
			i = 0
			while i<len(abbr):
				if abbr[i].isdigit():
					if i>=len(abbr)-1 or not abbr[i+1].isdigit():
						length+=1
				else:
					length+=1
				i+=1
			if length>=minLength: continue
			for i, word in enumerate(dictionary):
				if validWordAbbreviation(word, abbr): break
				if i==len(dictionary)-1: 
					minLength = length
					minAbbr = abbr
		return minAbbr