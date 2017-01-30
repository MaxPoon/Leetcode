public class Solution {
	public void rotate(int[] nums, int k) {
		k = k%nums.length;
		int [] sub1 = Arrays.copyOfRange(nums, 0, nums.length-k);
		int [] sub2 = Arrays.copyOfRange(nums, nums.length-k, nums.length);
		for(int i=0; i<nums.length;i++){
			if(i<k) nums[i]=sub2[i];
			else nums[i]=sub1[i-k];
		}
	}
}