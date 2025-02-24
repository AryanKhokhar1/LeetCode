class Solution {
    public boolean isStrictlyPalindromic(int n) {
        for(int i = 2; i<=n-2; i++){
            StringBuilder str = new StringBuilder();
            int num = n;
            while(num != 0){
                str.append(String.valueOf(num%i));
                num = num/i;
            }
            StringBuilder str1 = str;
            if(str1.equals(str.reverse())){
                return false;
            }
        }
        return true;
    }
}