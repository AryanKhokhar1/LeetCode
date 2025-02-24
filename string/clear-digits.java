class Solution {
    public String clearDigits(String s) {
        Stack<Character> stack = new Stack<>();
        int a;
        for(int i = 0; i<s.length(); i++){
            a = s.charAt(i);
            if((a>= 97 && a<123) || stack.isEmpty()){
                stack.push(s.charAt(i));
            }else{
                if(!stack.isEmpty() && (stack.peek()-'0' >= 7 && stack.peek()<123)){
                    stack.pop();
                }
            }
        }
        String ans = "";
        for(Character ch : stack){
            ans += ch;
        }
        return ans;
    }
}