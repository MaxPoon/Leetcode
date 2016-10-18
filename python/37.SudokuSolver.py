class Solution:
    """
    :type board: List[List[str]]
    :rtype: void Do not return anything, modify board in-place instead.
    """
    def solveSudoku(self, board):
        self.solve(0,board)
        
    def solve(self,cur,board):
        if cur==81:	return True
        
        i,j=cur/9,cur%9
        if board[i][j]!='.':	return self.solve(cur+1,board)
        
        for k in range(1,10):
            a=list(board[i])
            a[j]=str(k)
            board[i]=''.join(a)
            if self.check(i,j,board) and self.solve(cur+1, board):	return True     
            a[j]='.'   
            board[i]=''.join(a)
        return False
       
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
