class Solution {
    static boolean check_single_row(String word, char[] first_row, char[] second_row, char[] third_row){
        int p = 0;
        int q = 0;
        int r = 0;
        for(int i = 0; i<word.length(); i++){
            char letter = Character.toLowerCase(word.charAt(i));

            for(int a = 0; a<first_row.length; a++){
                if(letter == first_row[a]){
                    p++;
                }
            }
            for(int b = 0; b<second_row.length; b++){
                if(letter == second_row[b]){
                    q++;
                }
            }
            for(int c = 0; c<third_row.length; c++){
                if(letter == third_row[c]){
                    r++;
                }
            }
            if((p>0 && q>0) || (p>0 && r>0) || (q>0 && r>0) ){
                return false;
            }
        }
        return true;
    }
    public String[] findWords(String[] words) {
        ArrayList<String> answer = new ArrayList<String>();
        char[] first_row = {'q','w','e','r','t','y','u','i','o','p'};
        char[] second_row = {'a','s','d','f','g','h','j','k','l'};
        char[] third_row = {'z','x','c','v','b','n','m'};

        for(String word:words){
            boolean ans = check_single_row(word, first_row, second_row, third_row);
            if(ans == true){
                answer.add(word);
            }
        }
        for(String ele:answer){
            System.out.println(ele);
        }
        return answer.toArray(new String[0]);
    }
}