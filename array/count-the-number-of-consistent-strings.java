class Solution {
    public int countConsistentStrings(String allowed, String[] words) {
        
        HashMap<Character, Integer> allow = new HashMap<>();
        for(int i = 0; i<allowed.length(); i++){
            allow.put(allowed.charAt(i),1);
        }

        int answer = 0;
        boolean willadd;
        for(String word: words){
            willadd = true;
            for(int i = 0; i<word.length(); i++){
                if(allow.get(word.charAt(i)) == null){
                    willadd = false;
                    break;
                }
            }
            if(willadd){
                answer++;
            }
        }

        return answer;
    }
}