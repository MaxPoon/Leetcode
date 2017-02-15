public class Solution {
	public String addBinary(String a, String b) {
		if(a.length()==0) return b;
		if(b.length()==0) return a;
		if(a.charAt(a.length()-1)=='1' && b.charAt(b.length()-1)=='1') return addBinary(addBinary(a.substring(0, a.length()-1), b.substring(0, b.length()-1)), "1") + "0";
		if(a.charAt(a.length()-1)=='0' && b.charAt(b.length()-1)=='0') return addBinary(a.substring(0, a.length()-1), b.substring(0, b.length()-1)) + "0";
		return addBinary(a.substring(0, a.length()-1), b.substring(0, b.length()-1)) + "1";
	}
}