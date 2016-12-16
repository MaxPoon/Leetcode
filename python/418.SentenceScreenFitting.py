class Solution(object):
	def wordsTyping(self, sentence, rows, cols):
		"""
		:type sentence: List[str]
		:type rows: int
		:type cols: int
		:rtype: int
		"""
		sentence_string = " ".join(sentence)+" "
		start = 0
		l = len(sentence_string)
		r=0
		while r< rows:
			start += cols
			while sentence_string[start%l] != ' ':
					start -= 1
			start += 1
			r += 1
		return int(start/l)