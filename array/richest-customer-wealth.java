class Solution {
    public int maximumWealth(int[][] accounts) {
        int answer = Integer.MIN_VALUE;
        int wealth;
        for(int i = 0; i<accounts.length; i++){
            wealth =0;
            for(int j = 0; j<accounts[i].length; j++){
                wealth += accounts[i][j];
            }
            if(answer < wealth){
                answer = wealth;
            }
        }
        return answer;
    }
}