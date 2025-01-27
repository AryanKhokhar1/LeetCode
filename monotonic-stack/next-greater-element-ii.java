class Solution {
    public int[] nextGreaterElements(int[] nums) {
        int len = nums.length;
        int[] answer = new int[len];
        Arrays.fill(answer, -1);

        for(int i = 0; i<len; i++){
            
            int index = i+1;
            for(int j = 0; j<len; j++){
                if(index==len){
                    index = 0;
                }
                
                if(nums[index]>nums[i]){
                    answer[i] = nums[index];
                    break;
                }
                index++;

            }

        }
        return answer;
    }
}