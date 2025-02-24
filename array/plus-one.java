class Solution {
    public int[] plusOne(int[] digits) {
        boolean isadd = true;
        for(int i = digits.length-1; i>=0; i--){
            if(digits[i] == 9 && isadd == true){
                digits[i] = 0;
            }else if(digits[i] != 9 && isadd == true){
                digits[i] += 1;
                isadd = false;
            }
        }
        System.out.println(isadd);
        if(isadd == true){
            int answer[] = new int[digits.length+1];
            answer[0] = 1;
            for(int i = 1; i< digits.length+1; i++){
                answer[i] = 0;
            }
            return answer;
        }
        return digits;
    }
}