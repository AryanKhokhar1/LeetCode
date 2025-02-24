class Solution {
    public int minAddToMakeValid(String s) {
        
        Stack<Character> valid = new Stack<>();
        for(int i = 0; i<s.length(); i++){
            if(!valid.empty()){
                if((valid.peek() == '(' && s.charAt(i) == ')')){
                    valid.pop();
                    continue;
                }
            }
            valid.push(s.charAt(i));
        }
        return valid.size();
    }
}