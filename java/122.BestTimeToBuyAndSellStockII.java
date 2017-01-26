public class Solution {
	public int maxProfit(int[] prices) {
		int total = 0;
		if (prices.length<2) return 0;
		int start = 0;
		for(int i=1; i<prices.length; i++){
			if(prices[i]<prices[i-1]){
				total += prices[i-1]-prices[start];
				start = i;
			}
		}
		total += prices[prices.length-1]-prices[start];
		return total;
	}
}