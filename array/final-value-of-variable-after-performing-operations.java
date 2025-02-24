class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int X = 0;
        for(String element: operations){
            if(element.charAt(1) == '+'){
                X++;
            }else{
                X--;
            }
        }
        return X;
    }
}