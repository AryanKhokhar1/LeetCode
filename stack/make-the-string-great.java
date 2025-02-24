class Solution {
    public String makeGood(String s) {
        for(int i = 0; i<=s.length()-2; i++){
            if(Character.toUpperCase(s.charAt(i)) == Character.toUpperCase(s.charAt(i+1)) && (int) s.charAt(i) != (int) s.charAt(i+1) ){
                return makeGood(s.substring(0,i)+ s.substring(i+2));
            }
        }
        return s;
    }
}