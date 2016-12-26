public class Solution {
    public int hammingDistance(int x, int y) {
        int bit1, bit2, distance = 0;
        while(x>0 || y>0){
            bit1 = x & 1;
            bit2 = y & 1;
            if((bit1 ^ bit2) == 1) distance++;
            x>>=1;
            y>>=1;
        }
        return distance;
    }
}