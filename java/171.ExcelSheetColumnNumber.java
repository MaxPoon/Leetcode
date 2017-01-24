public class Solution {
	public int titleToNumber(String s) {
		int num = 0;
		for(int i=0; i<s.length(); i++){
			num*=26;
			char c = s.charAt(i);
			num += (int)c-64;
		}
		return num;
	}
}