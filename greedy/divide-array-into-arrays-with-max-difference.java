class Solution {
    public int[][] divideArray(int[] nums, int k) {
        int[][] answer = new int[nums.length/3][3];
        Arrays.sort(nums);
        int n = 0;
        for(int i = 0,j = 2; j<nums.length; i+=3 ,j+=3){
            if(nums[i] - nums[i+1] <=k && nums[i] - nums[j] <= k && nums[i+1] - nums[i] <=k && nums[i+1] - nums[j] <= k && nums[j] - nums[i] <=k && nums[j] - nums[i+1] <= k){
                System.out.println(i+","+(i+1)+","+j+","+n);
                answer[n][0] = nums[i];
                answer[n][1] = nums[i+1];
                answer[n][2] = nums[j];
                n++;
                System.out.println(nums[i]+","+nums[i+1]+","+nums[j]);
            }else{
                int[][] ans = new int[0][0];
                return ans;
            }
                
        }
        return answer;
    }
}