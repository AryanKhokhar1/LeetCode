class Solution {

    public String reverseParentheses(String s) {
        StringBuilder str = new StringBuilder(s);
        Stack<Character> stack = new Stack();
        int a = 0;
        char letter;
        StringBuilder sub = new StringBuilder();
        for(int i = 0; i<str.length(); i++){
            letter = str.charAt(i);
            if(letter == '('){
                a = i;
            }else if(letter == ')'){
                sub.append(str.substring(a+1,i));
                sub = sub.reverse();
                str.replace(a,i+1,sub.toString());
                sub.delete(0,sub.length());
                i = -1;
            }
        }
        return str.toString();
    }
}