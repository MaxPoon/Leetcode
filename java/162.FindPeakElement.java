public class Solution {
	public int findPeakElement(int[] nums) {
		if (nums.length == 1) return 0;
		if (nums[0]>nums[1]) return 0;
		int l = nums.length;
		if (nums[l-1] > nums[l-2]) return l-1;
		int left = 0;
		int right = l-1;
		int mid;
		while (left<right){
			mid = (left+right)/2;
			if (nums[mid-1]<nums[mid] && nums[mid]>nums[mid+1]) return mid;
			if (nums[mid-1]<nums[mid] && nums[mid]<nums[mid+1]) left = mid;
			else right = mid;
		}
		return right;
	}
}