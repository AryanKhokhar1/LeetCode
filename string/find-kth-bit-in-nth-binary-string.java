class Solution {
    private static String invert(String str){
        StringBuilder seq  = new StringBuilder();
        for(int i = 0; i<str.length(); i++){
            if(str.charAt(i) == '0'){
                seq.append('1');
            }else{
                seq.append('0');
            }
        }
        return seq.toString();
    }
    private static String strreverse(String str){
        return (new StringBuilder(str)).reverse().toString();
    }
    private String BinarySequence(int n){
        if(n == 1){
            return "0";
        }else{
            String prev = BinarySequence(n-1);
            return prev + "1"+ strreverse(invert(prev));
        }
    }
    public char findKthBit(int n, int k) {
        return BinarySequence(n).charAt(k-1);
    }
}