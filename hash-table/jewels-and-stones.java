class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        int ans = 0;
        for(int jew = 0; jew<jewels.length(); jew++){
            for(int sto = 0; sto<stones.length(); sto++){
                if(jewels.charAt(jew) == stones.charAt(sto)){
                    ans++;
                }
            }
        }
        return ans;
    }
}