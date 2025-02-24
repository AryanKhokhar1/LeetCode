class Solution {
    public int longestSubarray(int[] nums) {
        int a = Integer.MIN_VALUE;
        for(int element: nums){
            a = Math.max(a,element);
        }
        int count = 0;
        int ans = 0;
        for(int element: nums){
            if(element == a){
                count++;
            }else{
                count = 0;
            }
            ans = Math.max(count,ans);
        }
        return ans;
    }
}