public class Solution {
	public boolean canPartition(int[] nums) {
		int total = 0;
		for(int i=0; i<nums.length; i++)
			total += nums[i];
		if((total&1)==1) return false;
		boolean[][] dp = new boolean[nums.length][(total>>1)+1];
		for(int i=0; i<nums.length;i++) dp[i][0] = true;
		for(int i=0; i<nums.length; i++){
			for(int j=1; j<=total>>1; j++){
				if(i==0){
					if(nums[0]==j) dp[i][j] = true;
					else dp[i][j] = false;
				}else if(nums[i]<=j){
					dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i]];
				}else{
					dp[i][j] = dp[i-1][j];
				}
				if(j==total>>1 && dp[i][j]) return true;
			}
		}
		return false;
	}
}