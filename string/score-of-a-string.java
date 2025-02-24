class Solution {
    public int scoreOfString(String s) {
        
        int answer = 0;
        for(int i = 1; i<s.length(); i++){
            int digit1 = (int) s.charAt(i-1);
            int digit2 = (int) s.charAt(i);
            int sub = digit1 - digit2;
            if( (sub) < 0 ){
                sub = -sub;
            }
            answer = (sub) +answer;
        }
        return answer;
    }
}