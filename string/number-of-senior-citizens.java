class Solution {
    public int countSeniors(String[] details) {
        int ans = 0;
        for(String passanger: details){
            if(Integer.valueOf(passanger.substring(11,13)) > 60){
                ans++;
            }
        }
        return ans;
    }
}