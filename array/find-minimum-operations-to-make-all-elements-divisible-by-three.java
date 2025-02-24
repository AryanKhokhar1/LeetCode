class Solution {
    public int minimumOperations(int[] nums) {
        int op = 0;
        for(int ele: nums){
            if(ele%3 != 0){
                op++;
            }
        }
        return op;
    }
}