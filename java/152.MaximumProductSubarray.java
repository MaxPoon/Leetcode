public class Solution {
	public int maxProduct(int[] nums) {
		int max = nums[0], min = nums[0], result = nums[0];
		for (int i=1; i<nums.length; i++) {
			int temp = max;
			max = Math.max(Math.max(nums[i], nums[i]*max), nums[i]*min);
			min = Math.min(Math.min(nums[i], nums[i]*temp), nums[i]*min);
			if (max>result) result = max;
		}
		return result;
	}
}