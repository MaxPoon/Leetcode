public class Solution {
    public String reverseWords(String s) {
        int p1 = s.length()-1,p2 = s.length()-1;
        String reversed = "";
        while(true){
            while(p2>0 && s.charAt(p2)==' ') p2--;
            if(p2<0 || s.charAt(p2)==' ') break;
            p1 = p2;
            while(p1>0 && s.charAt(p1-1)!= ' ') p1--;
            if(reversed.length()>0) reversed += ' ';
            reversed += s.substring(p1,p2+1);
            p2 = --p1;
        }
        return reversed;
    }
}