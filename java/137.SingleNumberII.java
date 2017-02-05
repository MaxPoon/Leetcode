public class Solution {
	public int singleNumber(int[] nums) {
		int ans = 0;
		for (int i = 0; i < 32; i++)
		{
			int cnt = 0, bit = 1 << i;
			for (int j = 0; j < nums.length; j++)
			{
				if ((nums[j] & bit) == bit) cnt++;
			}
			if (cnt % 3 != 0)
				ans |= bit;
		}
	return ans;
	}
}