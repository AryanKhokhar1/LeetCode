class Solution {
    public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> answer = new ArrayList<>();
        answer.add(new ArrayList<>());
        int start = 0;
        int end = 0;
        for(int i = 0; i<nums.length; i++){
            start = 0;
            if(i > 0 && nums[i] == nums[i-1]){
                start = end;
            }
            end = answer.size();
            for(int j = start; j<end; j++){
                List<Integer> arr = new ArrayList<>(answer.get(j));
                arr.add(nums[i]);
                answer.add(arr);
            }
        }
        return answer;
    }
}