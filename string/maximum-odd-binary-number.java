class Solution {
    public String maximumOddBinaryNumber(String s) {
        int l = s.length();
        int one_count = 0;
        while(l-->0){
            if(s.charAt(l) == '1'){
                one_count++;
            }
        }
        String ans = "";
        int oc = one_count;
        while(--oc>0){
            ans = "1" + ans;
        }
        int zero = s.length()-one_count;
        while(zero-->0){
            ans = ans + "0";
        }
        ans = ans + "1";
        return ans;
    }
}