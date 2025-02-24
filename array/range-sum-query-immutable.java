class NumArray {
    private int[] prefix_array;
    public NumArray(int[] nums) {
        prefix_array = new int[nums.length+1];
        prefix_array[0] = 0;
        for(int i = 0; i<nums.length; i++){
            prefix_array[i+1] = prefix_array[i] + nums[i];
        }
    }
    
    public int sumRange(int left, int right) {
        if(left == 0){
            return prefix_array[right+1];
        }else{
            return  prefix_array[right+1] - prefix_array[left] ;
        }

    }
}

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray obj = new NumArray(nums);
 * int param_1 = obj.sumRange(left,right);
 */