class Solution {
    public boolean arrayStringsAreEqual(String[] word1, String[] word2) {
        StringBuffer wrd1 = new StringBuffer();
        StringBuffer wrd2 = new StringBuffer();
        for(String w1: word1){
            wrd1.append(w1);
        }
        for(String w2: word2){
            wrd2.append(w2);
        }
        return wrd1.toString().equals(wrd2.toString());
    }
}