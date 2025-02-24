class Solution {
    public int minBitFlips(int start, int goal) {

        int ans = start ^ goal;
        int answer = 0;
        while(ans!= 0){
            if((ans & 1) == 1){
                answer++;
            }
            ans = ans >> 1;
        }
        return answer;
    }
}