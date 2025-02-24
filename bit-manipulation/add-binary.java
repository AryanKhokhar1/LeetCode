class Solution {
    public String addBinary(String a, String b) {
        StringBuilder str = new StringBuilder();
        int carry = 0;
        for(int i = a.length()-1 , j = b.length()-1; i>= 0 || j>= 0; i--, j--){
            int first = 0;
            int second = 0;
            if(i>=0){
                first = a.charAt(i) - '0';
            }
            if(j>=0){
                second = b.charAt(j) - '0';
            }
            int sum = first + second + carry;
            if(sum < 2){
                str.insert(0,String.valueOf(sum));
                carry = 0;
            }else if(sum == 2){
                str.insert(0,"0");
                carry = 1;
            }else if(sum == 3){
                str.insert(0,"1");
                carry = 1;
            }
        }
        if(carry == 1){
            str.insert(0,"1");
        }

        return str.toString();
    }
}