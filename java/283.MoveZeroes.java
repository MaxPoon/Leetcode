public class Solution {
    public void moveZeroes(int[] nums) {
        int i=0, j=0;
        while(i<nums.length && j<nums.length){
            if(nums[i]==0 && nums[j]==0){
                j++;
            }
            else if(nums[i]==0 && nums[j]!=0){
                int temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                j++;
                i++;
            }
            else{
                i++;
                j++;
            }
        }
    }
}