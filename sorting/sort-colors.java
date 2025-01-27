class Solution {
    public void sortColors(int[] nums) {
        
        int a = 0;
        int b = 0;
        int c = 0;
        for(int i = 0; i<nums.length; i++){
            if(nums[i] == 0){
                a++;
            }else if(nums[i] == 1){
                b++;
            }else{
                c++;
            }
        }
        for(int i = 0; i<a; i++){
            nums[i] = 0;
        }
        for(int i = a; i<(b+a); i++){
            nums[i] = 1;
        }
        for(int i = (b+a); i<nums.length; i++){
            nums[i] = 2;
        }
    }
}