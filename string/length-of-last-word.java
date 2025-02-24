class Solution {
    public int lengthOfLastWord(String s) {
        String answer = "";
        boolean isAfterWord = false;
        char letter;
        for(int i = s.length()-1; i>=0; i--){
            letter = s.charAt(i);
            if(letter != ' '){
                answer = String.valueOf(letter) + answer ;
                isAfterWord = true;
            }
            if(letter == ' ' && isAfterWord == true){
                break;
            }
        }    
        return answer.length();    
    }
}