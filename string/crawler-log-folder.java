class Solution {
    public int minOperations(String[] logs) {
        int dist_from_main = 0;
        for(String ele: logs){
            if(ele.equals("../")){
                if(dist_from_main <= 0){

                }else{
                    dist_from_main--;
                }
            }else if(ele.equals("./")){

            }else{
                dist_from_main++;
            }
        }
        return dist_from_main;
    }
}