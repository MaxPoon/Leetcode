public class Solution {
	public int islandPerimeter(int[][] grid) {
		if (grid.length==0 || grid[0].length==0) return 0;
		int rows = grid.length;
		int cols = grid[0].length;
		int islands=0, repeats = 0;
		for(int row=0; row<rows; row++){
			for(int col=0; col<cols; col++){
				if(grid[row][col]==1){
					islands ++;
					if(row>0 && grid[row-1][col]==1) repeats++;
					if(col>0 && grid[row][col-1]==1) repeats++;
				}
			}
		}
		return 4*islands-2*repeats;
	}
}