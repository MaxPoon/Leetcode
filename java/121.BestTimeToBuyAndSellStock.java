public class Solution {
	public int maxProfit(int[] prices) {
		if(prices.length<2) return 0;
		int[] min = new int[prices.length];
		int[] max = new int[prices.length];
		int minOnLeft = prices[0];
		int maxOnRight = prices[prices.length-1];
		for(int i=0; i<prices.length;i++){
			if(prices[i]<minOnLeft) minOnLeft = prices[i];
			min[i] = minOnLeft;
		}
		for(int i=prices.length-1; i>0;i--){
			if(prices[i]>maxOnRight) maxOnRight = prices[i];
			max[i] = maxOnRight;
		}
		int maxDiff = 0;
		for(int i=0; i<prices.length; i++){
			maxDiff = Math.max(maxDiff, max[i]-min[i]);
		}
		return maxDiff;
	}
}