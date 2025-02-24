class Solution {
    public boolean isPalindrome(String s) {
        s = s.toLowerCase();
        StringBuilder str = new StringBuilder();
        char letter;
        for(int i = 0; i<s.length(); i++){
            letter = s.charAt(i);
            if(((int) letter < 123  && (int) letter > 96) || ((int) letter <58  && (int) letter > 47) ){
                str.append(letter);
            }
        }
        for(int i = 0, j = str.length()-1; i<=j; i++, j--){
            if(str.charAt(i) != str.charAt(j)){
                return false;
            }
        }
        return true;
    }
}