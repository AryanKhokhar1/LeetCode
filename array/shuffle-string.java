class Solution {
    public String restoreString(String s, int[] indices) {
        StringBuffer answer = new StringBuffer(s);
        for(int i = 0; i<indices.length; i++){
            answer.replace(indices[i],indices[i]+1,String.valueOf(s.charAt(i)));
        }
        return answer.toString();
    }
}