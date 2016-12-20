class Solution(object):
	def alienOrder(self, words):
		"""
		:type words: List[str]
		:rtype: str
		"""
		if len(words) == 0 : return ""
		if len(words)==1: return words[0]
		prev = {}
		next = {}
		charSet =set()
		added = ""
		for i in range(len(words)-1):
			word1 = words[i]
			word2 = words[i+1]
			p1 = 0
			p2 = 0
			while p1<len(word1) and p2<len(word2):
				charSet.add(word1[p1])
				charSet.add(word2[p2])
				if word1[p1] != word2[p2]: break
				p1+=1
				p2+=1
			if p2==len(word2) and p1<len(word1): return ""
			if p1==len(word1):
				while p2<len(word2):
					charSet.add(word2[p2])
					p2+=1
				continue
			if p2==len(word2):
				while p1<len(word1):
					charSet.add(word1[p1])
					p1+=1
				continue            
			c1 = word1[p1]
			c2 = word2[p2]
			while p1<len(word1):
				charSet.add(word1[p1])
				p1+=1
			while p2<len(word2):
				charSet.add(word2[p2])
				p2+=1
			if c1 in next:
				next[c1].append(c2)
			else:
				next[c1] = [c2]
			if c2 in prev:
				prev[c2].add(c1)
			else:
				prev[c2] = set(c1)
		l = len(charSet)
		print(charSet)
		while len(added)<l:
			if len(charSet)==0: break
			for c in charSet:
				if c not in prev or len(prev[c]) == 0:
					break
			if c in prev and len(prev[c]) != 0: return ""
			added += c
			charSet.remove(c)
			if c not in next: continue
			for c2 in next[c]:
				if c2 in prev and c in prev[c2]:
					prev[c2].remove(c)
		if len(added)<l: return ""  
		return added