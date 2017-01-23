public class Solution {
	public int[] productExceptSelf(int[] nums) {
		int product = 1;
		int zero = 0;
		for(int i=0; i<nums.length; i++) {
			if(nums[i]==0) zero++;
			else{
				product *= nums[i];
			}
		}
		if(zero>=2) for (int i=0; i<nums.length; i++) nums[i]=0;
		else if (zero==0)for(int i=0; i<nums.length; i++) nums[i] = product/nums[i];
		else{
			for(int i=0; i<nums.length; i++){
				if(nums[i]==0) nums[i]=product;
				else nums[i]=0;
			}
		}
		return nums;
	}
}