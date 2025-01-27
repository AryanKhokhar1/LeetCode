class Solution {
    public int[] vowelStrings(String[] words, int[][] queries) {
        ArrayList<Integer> prefixwords = new ArrayList<>();
        int[] answer = new int[queries.length];
        prefixwords.add(0);
        int prev = 0;
        char l;
        char r;
        for(int i = 0; i<words.length; i++){
            if((words[i].charAt(0) == 'a' ||
               words[i].charAt(0) == 'e' ||
               words[i].charAt(0) == 'i' ||
               words[i].charAt(0) == 'o' ||
               words[i].charAt(0) == 'u' ) &&


               (words[i].charAt(words[i].length() -1) == 'a' ||
               words[i].charAt(words[i].length() -1) == 'e' ||
               words[i].charAt(words[i].length() -1) == 'i' ||
               words[i].charAt(words[i].length() -1) == 'o' ||
               words[i].charAt(words[i].length() -1) == 'u' )
               ){
                prev++;

               }
            prefixwords.add(prev);
        }
        int a = 0;
        for(int i = 0; i<queries.length; i++){
            answer[a] = prefixwords.get((queries[i][1])+1) - prefixwords.get((queries[i][0]));
            a++;
        }
        return answer;
    }
}