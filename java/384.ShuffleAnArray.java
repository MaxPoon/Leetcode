public class Solution {
	int[] nums;
	int[] current;
	public Solution(int[] nums) {
		this.nums = nums;
		current = nums.clone();
	}
	
	/** Resets the array to its original configuration and return it. */
	public int[] reset() {
		current = nums.clone();
		return current;
	}
	
	/** Returns a random shuffling of the array. */
	public int[] shuffle() {
		for(int i=0; i<current.length-1; i++){
			int index = i + (int)(Math.random()*(current.length-i));
			int temp = current[i];
			current[i] = current[index];
			current[index] = temp;
		}
		return current;
	}
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(nums);
 * int[] param_1 = obj.reset();
 * int[] param_2 = obj.shuffle();
 */