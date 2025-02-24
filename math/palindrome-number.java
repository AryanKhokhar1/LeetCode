class Solution {
    public boolean isPalindrome(int x) {
        if(x<0){
            return false;
        }
        int prevx = x;
        int answer = 0;
        while(x != 0){
            int digit = x % 10;
            answer = (answer*10)+digit;
            x /= 10;
        }
        return prevx == answer;
    }
}