class Solution {
    public String[] uncommonFromSentences(String s1, String s2) {
        String[] arr1 = s1.split(" ");
        String[] arr2 = s2.split(" ");
        HashMap<String, Integer> map  =new HashMap<>();

        int size = 0;
        for(String ele: arr1){
            if(map.get(ele) == null){
                size++;
                map.put(ele,1);
            }else{
                if(map.get(ele) == 1){
                    size--;
                }
                map.put(ele,map.get(ele)+1);
            }
        }

        for(String ele: arr2){
            if(map.get(ele) == null){
                size++;
                map.put(ele,1);
            }else{
                if(map.get(ele) == 1){
                    size--;
                }
                map.put(ele,map.get(ele)+1);
            }
        }
        String[] ans = new String[size];
        int i = 0;
        for(Map.Entry<String, Integer> entry : map.entrySet()) {
            if(entry.getValue() == 1){
                ans[i++] = entry.getKey();
            }
        }
        return ans;
    }
}