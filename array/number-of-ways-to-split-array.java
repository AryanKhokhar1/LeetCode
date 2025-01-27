class Solution {
    public int waysToSplitArray(int[] nums) {
        // Here we create two prefix array 1. is right order and 2. is reverse order
        long[] preRightOrder = new long[nums.length];
        long[] preReverseOrder = new long[nums.length];
        long sum1 = 0;
        long sum2 = 0;
        for(int i = 0, j = nums.length -1; i<nums.length; i++, j--){
            sum1 += nums[i];
            sum2 += nums[j];
            preRightOrder[i] = sum1;
            preReverseOrder[j] = sum2;
        }

        int answer = 0;
        for(int i = 0; i<nums.length-1; i++){
            if(preRightOrder[i] >= preReverseOrder[i+1]){
                answer++;
            }
        }
        return answer;
    }
}