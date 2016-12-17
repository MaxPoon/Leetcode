class Solution(object):
	def reconstructQueue(self, people):
		"""
		:type people: List[List[int]]
		:rtype: List[List[int]]
		"""
		n = len(people)
		queue = []
		while len(queue)<n:
			highest = max(people, key=lambda x: x[0])[0]
			indexes = [i for i in range(len(people)) if people[i][0]==highest]
			news = []
			for index in indexes[::-1]:
				news.append(people.pop(index))
			news.sort(key=lambda x:x[1])
			for new in news:
				position = new[1]
				queue = queue[:position] + [new] + queue[position:]
		return queue