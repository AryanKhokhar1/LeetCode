class Solution {
    public String interpret(String command) {
        
        StringBuilder answer = new StringBuilder();
        for(int i = 0;i<command.length();){
            if(command.charAt(i) == 'G'){
                answer.append("G");
                i+=1;
            }else if(command.charAt(i) == '(' && command.charAt(i+1) == ')'){
                answer.append("o");
                i+=2;
            }else{
                answer.append("al");
                i+=4;
            }
        }
        return answer.toString();
    }
}