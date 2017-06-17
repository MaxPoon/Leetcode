import string
from collections import defaultdict
class Solution(object):
	def findLadders(self, beginWord, endWord, wordList):
		"""
		:type beginWord: str
		:type endWord: str
		:type wordList: List[str]
		:rtype: List[List[str]]
		"""
		wordList = set(wordList)
		if endWord not in wordList: return []
		if beginWord in wordList: wordList.remove(beginWord)
		if endWord in wordList: wordList.remove(endWord)
		beginSet, endSet = set([beginWord]), set([endWord])
		
		ansFound = False
		mp = defaultdict(list)
		while beginSet and endSet:
			if len(beginSet) < len(endSet):
				isBeginSmall, small, big = True, beginSet, endSet
			else:
				isBeginSmall, small, big = False, endSet, beginSet
			
			nextlvl = set([])
			for word in small:
				for i in range(len(word)):
					for char in string.lowercase:
						newword = word[:i] + char + word[i+1:]
						
						if newword in big or newword in wordList:
							if newword in big: 
								ansFound = True
							nextlvl.add(newword)
							if isBeginSmall: mp[word].append(newword)
							else: mp[newword].append(word)
			
			if ansFound: break
			for word in nextlvl:
				wordList.remove(word)
			if isBeginSmall: beginSet = nextlvl
			else: endSet = nextlvl
		
		if not ansFound: return []
		
		res = [[beginWord]]
		while res[0][-1] != endWord:
			tmp = res
			res = []
			for line in tmp:
				for word in mp[line[-1]]:
					res.append(line + [word])
		return res