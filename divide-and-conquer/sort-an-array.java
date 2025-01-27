class Solution {

    static int[] merge(int[] first, int[] second){
        int[] mix = new int[first.length + second.length];
        int i = 0;
        int j = 0;
        int x = 0;
        while(i<first.length && j<second.length){
            if(first[i] < second[j]){
                mix[x++] = first[i++];
            }else{
                mix[x++] = second[j++];
            }
        }

        while(i<first.length){
            mix[x++] = first[i++];
        }
        while(j<second.length){
            mix[x++] = second[j++];
        }
        return mix;
    }

    public int[] sortArray(int[] nums) {
        if(nums.length == 1){
            return nums;
        }

        int mid = nums.length/2;
        int[] left = sortArray(Arrays.copyOfRange(nums, 0, mid));
        int[] right = sortArray(Arrays.copyOfRange(nums,mid,nums.length));

        return merge(left,right);
    }
}