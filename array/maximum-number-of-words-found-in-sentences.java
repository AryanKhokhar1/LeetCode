class Solution {
    public int mostWordsFound(String[] sentences) {
        int ans = -1;
        for(String word: sentences){
            String[] val = word.split(" ",-2);
            if(ans<val.length){
                ans = val.length;
            }
        }
        return ans;
    }
}