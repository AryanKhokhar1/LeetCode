class Solution {
    public boolean canBeEqual(int[] target, int[] arr) {
        HashMap<Integer, Integer> map = new HashMap<>();
        for(int ele: target){
            if(map.get(ele) == null){
                map.put(ele,1);
            }else{
                map.put(ele,map.get(ele)+1);
            }
        }

        for(int ele: arr){
            if(map.get(ele) == null){
                return false;
            }else{
                if(map.get(ele) == 1){
                    map.remove(ele);
                }else{
                    map.put(ele,map.get(ele)-1);
                }
            }
        }

        return true;
    }
}