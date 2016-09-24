class Solution:
    """
    Calculate the total number of distinct N-Queen solutions
    @param n: The number of queens.
    @return: The total number of distinct solutions.
    """
    total = 0
    n = 0

    def attack(self, row, col):
        for c, r in self.cols.iteritems():
            if c - r == col - row or c + r == col + row:
                return True
        return False

    def search(self, row):
        if row == self.n:
            self.total += 1
            return
        for col in range(self.n):
            if col in self.cols:
                continue
            if self.attack(row, col):
                continue
            self.cols[col] = row
            self.search(row + 1)
            del self.cols[col]

    def totalNQueens(self, n):
        self.n = n
        self.cols = {}
        self.search(0)
        return self.total
        
