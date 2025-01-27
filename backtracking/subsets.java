class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> ans = new ArrayList<>();
        ans.add(new ArrayList<>());

        for(int ele: nums){
            int len = ans.size();
            for(int i = 0; i<len; i++){
                ArrayList<Integer> temp = new ArrayList<>(ans.get(i));
                temp.add(ele);
                ans.add(temp);
            }
        }
        return ans;
    }
}