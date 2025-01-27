class Solution {
    public void rotate(int[] nums, int k) {
            k = k%nums.length;
            int[] newNums = new int[nums.length];
            int i = 0;
            int diff = nums.length - k;
            for(; i<k && i<nums.length ; i++){
                newNums[i] = nums[diff++];
            }
            int p = 0;
            for(;i<nums.length; i++){
                newNums[i] = nums[p++];
            }
            System.arraycopy(newNums, 0, nums, 0, newNums.length);
    }
}