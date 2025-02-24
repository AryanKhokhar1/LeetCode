class Solution {
    public int findComplement(int num) {
        int answer = 0;
        int n = 0;
        while(num != 0){
            if((num&1) == 0){
                answer += (int) Math.pow(2,n);
            }
            num = num >> 1;
            n++;
        }
        return answer;
    }
}