def findRoot(num, union):
	depth = 0
	# while union[num] != num and union[num] != union[union[num]]:
	#     union[num] = union[union[num]]
	#     depth += 1
	# return (union[num], depth)  
	while union[num]!=num:
		num = union[num]
		depth+=1
	return (num, depth)

class Solution(object):
	def longestConsecutive(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		union = {}
		for n in nums:
			in1 = n+1 in union
			in2 = n-1 in union
			if not in1 and not in2:
				union[n] = n
			elif in1 and in2:
				root1, depth1 = findRoot(n+1, union)
				root2, depth2 = findRoot(n-1, union)
				print(root1, root2)
				if depth1<depth2:
					union[root1] = root2
					union[n] = root2
				else:
					union[root2] = root1
					union[n] = root1
			else:
				if in1: num = n+1
				else: num = n-1
				root, depth = findRoot(num, union)
				union[n] = root
		count = {}
		for value in union.values():
			root, depth = findRoot(value, union)
			count[root] = count.get(root,0)+1
		return max(count.values())