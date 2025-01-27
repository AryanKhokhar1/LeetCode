class Solution {
    public void reverseString(char[] s) {
        int sl = s.length;
        for(int i = 0; i<sl/2; i++){
            char store = s[i];
            s[i] = s[sl-i-1];
            s[sl-i-1] = store;
        }
    }
}