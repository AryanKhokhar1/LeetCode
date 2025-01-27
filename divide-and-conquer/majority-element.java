class Solution {
    public int majorityElement(int[] nums) {
        HashMap<Integer,Integer> max_Count = new HashMap<>();
        int value;
        for(int ele:nums){
            if(!max_Count.containsKey(ele)){
                max_Count.put(ele,1);
            }else{
                value = max_Count.get(ele)+1;
                max_Count.replace(ele,value);
            }
        }
        int answerKey= -1;
        int answerValue = -1;
        for (Map.Entry<Integer, Integer> map :max_Count.entrySet()) {
            if(map.getValue() > answerValue){
                answerValue = map.getValue();
                answerKey = map.getKey();
            }
        }
        return answerKey ;
    }
}