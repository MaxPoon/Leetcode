class Solution(object):
	def gameOfLife(self, board):
		"""
		:type board: List[List[int]]
		:rtype: void Do not return anything, modify board in-place instead.
		"""
		if board is None or len(board)==0 or len(board[0])==0: return
		rows = len(board)
		cols = len(board[0])
		for row in range(rows):
			for col in range(cols):
				live = 0
				for r in range(row-1, row+2,1):
					for c in range(col-1,col+2,1):
						if (r==row and c==col) or r<0 or c<0 or r>=rows or c>=cols: continue
						if board[r][c]&1==1: live+=1
				if live==2 and board[row][col]==1:
					board[row][col]+=2
				if live==3:
					board[row][col]+=2
				if row>0 and col>0: board[row-1][col-1]>>=1
		for col in range(cols):
			board[-1][col]>>=1
		for row in range(rows-1):
			board[row][-1]>>=1