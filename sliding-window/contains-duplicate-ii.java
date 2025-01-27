class Solution {
    public boolean containsNearbyDuplicate(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();

        for(int i = 0; i<nums.length; i++){
            if(map.get(nums[i]) == null){
                map.put(nums[i],i);
            }else{
                if(i-map.get(nums[i]) <= k){
                    return true;
                }
                map.put(nums[i],i);
            }
        }
        return false;
    }
}