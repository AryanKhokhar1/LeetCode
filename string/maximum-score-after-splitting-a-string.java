class Solution {
    public int maxScore(String s) {
        
        int a = 0;
        int answer = 0;
        int intervalscor;
        for(int i = 0; i<s.length()-1; i++){
            intervalscor = 0;
            for(int j = 0; j<s.length(); j++){
                if(j<=a){
                    if(s.charAt(j) - '0' == 0){
                        intervalscor++;
                    }
                }else{
                    if(s.charAt(j) - '0' == 1){
                        intervalscor++;
                    }
                }
            }
            answer = Math.max(intervalscor,answer);
            a++;
        }

        return answer;
    }
}