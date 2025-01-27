class Solution {
    public int[] decrypt(int[] code, int k) {
        int[] answer = new int[code.length];
        if(k<0){
            k *= -1;
            for(int i = answer.length-1; i>=0; i--){         
                for(int a = 1; a<=k; a++){
                    if(i>=a){
                        answer[i] += code[(i-a)%answer.length];
                    }else{
                        answer[i] += code[answer.length - (a-i)];
                    }
                }
            }
        }else if( k == 0){
            Arrays.fill(answer,0);
        }else{
            for(int i = 0; i<answer.length; i++){         
                for(int a = 1; a<=k; a++){
                    answer[i] += code[(i+a)%answer.length];
                }
            }
        }
        return answer;
    }
}