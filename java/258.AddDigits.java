public class Solution {
	public int addDigits(int num) {
		if(num==0) return 0;
		int n = num%9;
		if (n!= 0) return n;
		return 9;
	}
}