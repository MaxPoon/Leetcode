public class Solution {
    public boolean repeatedSubstringPattern(String str) {
        int[] prefix = kmp(str);
        int len = prefix[str.length()-1];
        int n = str.length();
        return (len > 0 && n%(n-len) == 0);
    }
    private int[] kmp(String s){
        int len = s.length();
        int[] res = new int[len];
        char[] ch = s.toCharArray();
        int i = 0, j = 1;
        res[0] = 0;
        while(i < ch.length && j < ch.length){
            if(ch[j] == ch[i]){
                res[j] = i+1;
                i++;
                j++;
            }else{
                if(i == 0){
                    res[j] = 0;
                    j++;
                }else{
                    i = res[i-1];
                }
            }
        }
        return res;
    }
}