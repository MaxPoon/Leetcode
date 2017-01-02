public class Solution {
	public boolean isOneEditDistance(String s, String t) {
		if(Math.abs(s.length()-t.length())>=2) return false;
		int i = 0, j = 0, d = 0;
		while(i<s.length() && j<t.length()){
			if(s.charAt(i)!=t.charAt(j)){
				if(++d>1) return false;
				if(s.length()==t.length()){
					i++;
					j++;
				}
				else if(s.length()>t.length()) i++;
				else j++;
			}
			else{
				i++;
				j++;
			}
		}
		if(i<s.length() || j<t.length()) d++;
		if(d==1) return true;
		else return false;
	}
}