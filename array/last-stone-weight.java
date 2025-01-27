class Solution {
    public int lastStoneWeight(int[] stones) {
        ArrayList<Integer> list = new ArrayList<Integer>();
        for(int stone: stones){
            list.add(stone);
        }
        while(list.size()>1){
            Collections.sort(list,Collections.reverseOrder());
            if(list.get(0) != list.get(1)){
                list.add(list.get(0)-list.get(1));
            }
            list.remove(0);
            list.remove(0);
        }
        if(list.size() == 0){
            return 0;
        }else{
        return list.get(0);
        }
    }
}