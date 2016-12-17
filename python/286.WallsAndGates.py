class Solution(object):
	def wallsAndGates(self, rooms):
		"""
		:type rooms: List[List[int]]
		:rtype: void Do not return anything, modify rooms in-place instead.
		"""
		if rooms is None or len(rooms) == 0 or len(rooms[0])==0: return 
		rows = len(rooms)
		cols = len(rooms[0])
		gates=[]
		for r in range(rows):
			for c in range(cols):
				if rooms[r][c] == 0: gates.append((r,c))
		while gates:
			row, col = gates.pop()
			open_state = [(row,col, 0)]
			while open_state:
				row, col, d = open_state.pop(0)
				for (r,c) in ((row+1,col),(row-1,col),(row,col+1),(row,col-1)):
					if 0<= r<rows and 0<= c<cols and rooms[r][c]>d+1:
						rooms[r][c]=d+1
						open_state.append((r,c,d+1))