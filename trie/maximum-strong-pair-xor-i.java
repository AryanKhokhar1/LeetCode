class Solution {
    public int maximumStrongPairXor(int[] nums) {
        
        int ans = 0;
        int diff;
        for(int i = 0; i<nums.length; i++){
            for(int j = i; j<nums.length; j++){
                if(nums[i]>=nums[j]){
                    diff = nums[i] - nums[j];
                }else{
                    diff = -1 * (nums[i] - nums[j]);
                }
                if(diff <= Math.min(nums[i],nums[j])){
                    ans = Math.max(ans,nums[i] ^ nums[j]);
                }
            }
        }
        return ans;
    }
}