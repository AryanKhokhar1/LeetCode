class Solution {
    private int backtrack(int index, int current_or, int[] nums, int max_or){
        if(index == nums.length){
            if(current_or == max_or){
                return 1;
            }else{
                return 0;
            }
        }
        int include = backtrack(index+1, current_or | nums[index], nums, max_or);
        int exclude = backtrack(index + 1, current_or, nums, max_or);
        return include + exclude;
    }
    public int countMaxOrSubsets(int[] nums) {
        int max_bit_or = 0;
        for(int number: nums){
            max_bit_or = max_bit_or | number;
        }
        return backtrack(0,0,nums,max_bit_or);
    }
}