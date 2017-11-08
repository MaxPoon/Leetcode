class Solution(object):
	def isPossible(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		counts = [(x, len(list(group))) for x, group in itertools.groupby(nums)]

		def possible(chunk):
			l = len(chunk)
			if l < 3: return False
			starts, ends = [0]*l, [0]*l
			starts[0] = chunk[0]
			for i in range(l):
				if i > 0 and chunk[i] > chunk[i-1]:
					starts[i] = chunk[i] - chunk[i-1]
				if i < l-1 and chunk[i] > chunk[i+1]:
					ends[i] = chunk[i] - chunk[i+1]
			if ends[0] or ends[1]: return False
			if starts[-2] or starts[-1]: return False
			sequences = 0
			for i in range(l):
				if sequences < starts[i-2] + starts[i-1]:
					return False
				sequences -= ends[i]
				sequences += starts[i]
			return True
			

		chunk = []
		prev = None
		for x, count in counts:
			if prev is None or x - prev == 1:
				chunk.append(count)
			else:
				if not possible(chunk):
					return False
				chunk = []
			prev = x

		return possible(chunk)
