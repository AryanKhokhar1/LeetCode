class Solution {
    public int[] rearrangeArray(int[] nums) {
        int[] ans = new int[nums.length];
        int i = 0;
        int j = 1;
        for(int ele:nums){
            if(ele>0){
                ans[i] = ele;
                i += 2;
            }else{
                ans[j] = ele;
                j += 2;
            }
        }
        return ans;
    }
}