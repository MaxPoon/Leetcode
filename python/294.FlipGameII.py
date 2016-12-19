def generatePossibleNextMoves(s):
	if len(s)<2: return []
	moves = []
	for i in range(1,len(s)):
		if s[i-1:i+1] == "++":
			moves.append(s[:i-1] + "--" + s[i+1:])
	return moves

def dfs(s, results, depth):
	player = depth & 1
	moves = generatePossibleNextMoves(s)
	if len(moves) == 0:
		results[s] = False if player==0 else True
		return
	for move in moves:
		if move not in results:
			dfs(move, results, depth+1)
		if results[move] and player==0:
			results[s] = True
			return
		elif not results[move] and player==1:
			results[s] = False
			return
	if player == 0:
		results[s] = False
	else:
		results[s] = True

class Solution(object):
	def canWin(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		results = {}
		dfs(s, results, 0)
		return results[s]