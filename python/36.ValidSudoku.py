class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            for j in range(9):
                if board[i][j]!='.' and not self.check(i,j,board): return False
        return True
        
    def check(self,x,y,board):
        for i in range(0,9):
            if board[x][i]==board[x][y] and i!=y or board[i][y]==board[x][y] and i!=x:
                return False
        r=x/3*3
        c=y/3*3
        for i in range(0,3):
            for j in range(0,3):
                if board[r + i][c + j] == board[x][y] and x != r + i and y != c + j:
                    return False
        return True
