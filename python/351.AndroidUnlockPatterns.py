def search(jumpTable, visited, current, keys, m, n):
	if keys==n: return 1
	result = 1 if keys>= m else 0
	for i in range(1,10):
		if not visited[i] and current != i and ((current, i) not in jumpTable or visited[jumpTable[(current,i)]]):
			visited[i]=True
			result += search(jumpTable, visited, i, keys+1, m, n)
			visited[i] = False
	return result

class Solution(object):
	def numberOfPatterns(self, m, n):
		"""
		:type m: int
		:type n: int
		:rtype: int
		"""
		jumpTable = {}
		jumpTable[(1,3)] = 2
		jumpTable[(1,7)] = 4
		jumpTable[(1,9)] = 5
		jumpTable[(3,1)] = 2
		jumpTable[(3,9)] = 6
		jumpTable[(3,7)] = 5
		jumpTable[(7,1)] = 4
		jumpTable[(7,9)] = 8
		jumpTable[(7,3)] = 5
		jumpTable[(9,3)] = 6
		jumpTable[(9,7)] = 8
		jumpTable[(9,1)] = 5
		jumpTable[(2,8)] = 5
		jumpTable[(8,2)] = 5
		jumpTable[(4,6)] = 5
		jumpTable[(6,4)] = 5
		result = 0
		visited = [False]*10
		visited[1]=True
		result += 4*search(jumpTable, visited, 1, 1, m, n)
		visited[1] = False
		visited[2] = True
		result += 4*search(jumpTable, visited, 2, 1, m, n)
		visited[2]=False
		visited[5]=True
		result += search(jumpTable, visited, 5, 1, m, n)
		return result