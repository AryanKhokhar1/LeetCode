class Solution {
    public List<String> cellsInRange(String s) {
        List<String> answer = new ArrayList<String>();
        String firstword = s.substring(0,2);
        String secondword = s.substring(3,s.length());
        char first_letter = firstword.charAt(0);
        char second_letter = secondword.charAt(0);
        int first_num = Integer.parseInt(firstword.substring(1));
        int second_num = Integer.parseInt(secondword.substring(1)); 
        // System.out.println(first_letter+"\n"+second_letter+"\n"+first_num+"\n"+second_num);
        while(first_letter <= second_letter){
            for(int i = first_num; i<= second_num; i++){
                // System.out.println("inner");
                answer.add(first_letter+String.valueOf(i));
            }
            first_letter++;
        }

        return answer;
    }
}