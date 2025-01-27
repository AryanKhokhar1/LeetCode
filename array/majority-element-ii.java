class Solution {
    public List<Integer> majorityElement(int[] nums) {
        HashMap<Integer,Integer> map = new HashMap<>();
        for(int element: nums){
            if(map.get(element) == null){
                map.put(element,1);
            }else{
                map.put(element,map.get(element)+1);
            }
        }
        
        List<Integer> arrayList = new ArrayList<>();
        int val = nums.length/3;
        for(int ele: nums){
            if(map.get(ele)>val){
                arrayList.add(ele);
                map.put(ele,-1);
            }
        }

        return arrayList;
    }
}