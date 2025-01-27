class Solution {
    public int maxProfit(int[] prices) {
        // int max = 0;
        // int min = prices[0];
        int answer = 0;
        if(prices.length == 1){
            return 0;
        }
        for(int i = 0, j= 1; j<prices.length;i++,j++){
            if(prices[j]>prices[i]){
                answer += prices[j] - prices[i];
            }
        }
        return answer;
    }
}