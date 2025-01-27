class Solution {
    private StringBuilder word = new StringBuilder("a");
    public char kthCharacter(int k) {
        if(word.length() >= k){
            return word.charAt(k-1);
        }
        int len = word.length();
        for(int i = 0; i<len; i++){
            word.append((char)((word.charAt(i) + 1)));
        }
        return kthCharacter(k);
    }
}