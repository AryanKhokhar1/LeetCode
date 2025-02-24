class Solution {
    public String decodeMessage(String key, String message) {
        StringBuffer answer = new StringBuffer();
        Map<Character, Character> table = new HashMap<>();
        char letter = 'a';
        for(int i =0; i<key.length(); i++){
            if(table.containsKey(key.charAt(i)) || key.charAt(i) == ' '){
                continue;
            }else{
                table.put(key.charAt(i),letter);
                letter++;
            }
        }
        System.out.println(table);
        for(int i =0; i<message.length(); i++){
            if(message.charAt(i) == ' '){
                answer.append(" ");
            }else{
                answer.append(table.get(message.charAt(i)));
            }
        }
        return answer.toString();
    }
}