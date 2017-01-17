public class Solution {
	public int maxArea(int[] height) {
		int p1 = 0, p2 = height.length-1;
		int maxwater = 0;
		while(p1<p2){
			int water = (p2-p1)*Math.min(height[p1],height[p2]);
			maxwater = Math.max(maxwater,water);
			if(height[p1]>height[p2]) p2--;
			else p1++;
		}
		return maxwater;
	}
}