public class Solution {
	public int maxSubArray(int[] nums) {
		int dp[] = new int[nums.length];
		dp[0] = nums[0];
		for(int i=1; i<nums.length; i++){
			if(dp[i-1]<0) dp[i] = nums[i];
			else dp[i] = nums[i] + dp[i-1];
		}
		int max = dp[0];
		for(int i=1; i<nums.length; i++){
			max = Math.max(max, dp[i]);
		}
		return max;
	}
}