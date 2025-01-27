class Solution {
    public int maxArea(int[] height) {
        int answer = 0;
        for(int i = 0, j= height.length-1; i<j;){
            if(Math.min(height[i],height[j])*(j-i) > answer){
                answer = Math.min(height[i],height[j])*(j-i);
            }
            if(height[i]<height[j]){
                i++;
            }else{
                j--;
            }
        }
        return answer;
    }
}