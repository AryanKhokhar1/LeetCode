class Solution {
    public int[] twoSum(int[] numbers, int target) {
        for(int i = 0, j= numbers.length -1; i<j; ){
            if(target == numbers[i] + numbers[j]){
                return new int[]{i+1,j+1};
            } else if(target > numbers[i]+numbers[j]){
                i++;
            }else if(target < numbers[i] + numbers[j]){
                j--;
            }
            // System.out.println(i+":"+j);
        }
        return new int[]{};
    }
}