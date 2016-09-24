class Solution(object):
    n = 0
    result = []
    
    def addBoard(self):
        board = [""]*self.n
        for c,r in self.cols.iteritems():
            board[r] = c*"."+"Q"+(self.n-1-c)*"."
        self.result.append(board)

    def attack(self, row, col):
        for c, r in self.cols.iteritems():
            if c - r == col - row or c + r == col + row:
                return True
        return False

    def search(self, row):
        if row == self.n:
            self.addBoard()
            return
        for col in range(self.n):
            if col in self.cols:
                continue
            if self.attack(row, col):
                continue
            self.cols[col] = row
            self.search(row + 1)
            del self.cols[col]

    def solveNQueens(self, n):
        self.result = []
        self.n = n
        self.cols = {}
        self.search(0)
        return self.result
