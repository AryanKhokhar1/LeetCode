class Solution {
    public List<String> summaryRanges(int[] nums) {
        List<String> answer = new ArrayList<>();
        if(nums.length == 0){
            return new ArrayList<>();
        }
        int startVal = nums[0];
        int prevVal = nums[0];
        String newStr;
        for(int i = 1; i<nums.length; i++){
            if(prevVal+1 != nums[i]){
                if(prevVal == startVal){
                    answer.add(String.valueOf(prevVal));
                }else{
                    newStr = String.format("%d->%d",startVal,prevVal);
                    answer.add(newStr);
                }
                startVal = nums[i];
                prevVal = nums[i];
            }else{
                prevVal = nums[i];
            }


            
        }
        if(prevVal == startVal){
            answer.add(String.valueOf(prevVal));
        }else{
            newStr = String.format("%d->%d",startVal,prevVal);
            answer.add(newStr);
        }
        return answer;
    }
}