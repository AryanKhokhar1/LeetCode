class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int answer = 0;
        int val = 0;
        for(int i = 0; i<nums.length; i++){
            if(nums[i] == 0){
                answer = Math.max(answer,val);
                val = 0;
            }else{
                val += 1;
            }
        }
        answer = Math.max(answer, val);
        return answer;
    }
}