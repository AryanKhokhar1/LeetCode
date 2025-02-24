class Solution {
    public String kthDistinct(String[] arr, int k) {
        LinkedHashMap<String, Integer> map = new LinkedHashMap<>();

        for(String ele: arr){
            if(map.get(ele) == null){
                map.put(ele,1);
            }else{
                map.put(ele,map.get(ele)+1);
            }
        }
        String[] key = map.keySet().toArray(new String[0]);
        for(String element : key){
            if(map.get(element) == 1){
                --k;
            }
            if(k == 0){
                return element;
            }
        }
        return "";
    }
}