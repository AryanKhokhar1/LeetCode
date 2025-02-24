class Solution {
    public int[] minOperations(String boxes) {
        
        int answer[] = new int[boxes.length()];
        for(int i = 0; i<answer.length; i++){
            int cost = 0;
            for(int j = 0; j<boxes.length(); j++){
                if(boxes.charAt(j) == '1'){
                    cost = Math.abs(j-i)+ cost;
                }
            }
            answer[i] = cost;
        }
        return answer;
    }
}