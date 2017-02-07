public class Solution {
	public int countBattleships(char[][] board) {
		int ships = 0;
		for(int i=0; i<board.length; i++){
			boolean foundShip = false;
			for(int j=0; j<board[0].length; j++){
				if(board[i][j]=='X'){
					if(!foundShip && (j<board[i].length-1) && board[i][j+1]=='X'){
						ships++;
						foundShip = true;
					}
				}else{
					foundShip = false;
				}
			}
		}
		for(int i=0; i<board[0].length; i++){
			boolean foundShip = false;
			for(int j=0; j<board.length; j++){
				if(board[j][i]=='X'){
					if(!foundShip && (i==0 || board[j][i-1]=='.') && (i==board[j].length-1 || board[j][i+1]=='.')){
						ships++;
						foundShip = true;
					}
				}else{
					foundShip = false;
				}
			}
		}
		return ships;
	}
}