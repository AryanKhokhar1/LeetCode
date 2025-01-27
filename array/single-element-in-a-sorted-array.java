class Solution {
    public int singleNonDuplicate(int[] nums) {
        int answer = 0;
        for(int ele:nums){
            answer = answer ^ ele;
        }
        return answer;
    }
}