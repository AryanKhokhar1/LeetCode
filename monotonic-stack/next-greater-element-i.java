class Solution {
    public int[] nextGreaterElement(int[] nums1, int[] nums2) {
        int[] answer = new int[nums1.length];
        Arrays.fill(answer, -1);
        for(int i = 0; i<nums1.length; i++){
            boolean meet = false;
            for(int element2: nums2){
                if(meet && element2 > nums1[i]){
                    answer[i] = element2;
                    break;
                }
                if(nums1[i] == element2){
                    meet = true;
                }
                
            }
        }

        return answer;

    }
}