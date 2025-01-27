class Solution {
    public long minimumSteps(String s) {
        
        // position - a(Number of 1 face)
        int a = 0;
        long answer = 0;
        for(int i = s.length()-1; i>= 0;  i--){
            if(s.charAt(i) == '1'){
                answer = answer + ((s.length() - i -1) - a);
                a++;
            }
        }
        return answer;
    }
}