class Solution {
    private static int setBit(int num){
        int result = 0;
        while(num != 0){
            if((num & 1) == 1){
                result++;
            }
            num = num >> 1;
        }
        return result;
    }
    public boolean canSortArray(int[] nums) {
        if(nums.length<=1){
            return true;
        }
        int prev = setBit(nums[0]);
        int maxValue = 0;
        int anotherMax = nums[0];
        for(int i = 1; i<nums.length; i++){
            if(prev != setBit(nums[i])){
                if(anotherMax > nums[i]){
                    return false;
                }
                maxValue = anotherMax;
                anotherMax = nums[i];
            } else {
                if(maxValue > nums[i]){
                    return false;
                }
                anotherMax = Math.max(nums[i],anotherMax);
            }
            prev = setBit(nums[i]);
        }
        return true;
    }
}