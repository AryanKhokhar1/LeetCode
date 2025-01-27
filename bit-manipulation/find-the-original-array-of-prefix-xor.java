class Solution {
    public int[] findArray(int[] pref) {
        int x = pref[0];
        int a ;
        for(int i = 1; i<pref.length; i++){
            a = pref[i];
            pref[i] = pref[i] ^ x;
            x = a;
        }
        return pref;
    }
}