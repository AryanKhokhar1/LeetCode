class Solution {
    public boolean isValid(String s) {
        Stack<Character> store_par = new Stack<>();
        char letter;
        // if(s.charAt(0) == ')' || s.charAt(0) == ']' || s.charAt(0) == '}'){
        //     return false;
        // }
        for(int i = 0; i<s.length(); i++){
            letter = s.charAt(i);
            if(letter == '(' || letter == '[' || letter == '{'){
                store_par.push(letter);
            }else if(!store_par.isEmpty()){
                if(store_par.peek() == '(' && letter == ')'){
                    store_par.pop();
                }else if(store_par.peek() == '[' && letter ==  ']'){
                    store_par.pop();
                }else if(store_par.peek() == '{' && letter == '}'){
                    store_par.pop();
                }else{
                    return false;
                }
            }else if((store_par.isEmpty() && letter == '}') || (store_par.isEmpty() && letter == ')')|| (store_par.isEmpty() && letter == ']')){
                return false;
            }
        }
        if(store_par.isEmpty()){
            return true;
        }
        return false;
    }
}