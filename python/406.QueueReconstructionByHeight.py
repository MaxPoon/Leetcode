class Solution(object):
	def reconstructQueue(self, people):
		"""
		:type people: List[List[int]]
		:rtype: List[List[int]]
		"""
		n = len(people)
		for i in range(n):
			people[i].append(people[i][1])
		queue = []
		while len(queue)<n:
			lowest = -1
			lowest_i = -1
			i = 0
			while i< len(people):
				h,k = people[i][0], people[i][2]
				if  k==0 and (h<lowest or lowest==-1):
					lowest = h
					lowest_i = i
				i+=1
			lowest,k,k2 = people.pop(lowest_i)
			queue.append((lowest,k))
			for i in range(len(people)):
				if people[i][0]<=lowest:
					people[i][2]-=1
		return queue