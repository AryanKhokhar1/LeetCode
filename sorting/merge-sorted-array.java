class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        if(nums2.length == 0){
            return;
        }
        int b = 0;
        for(;m<nums1.length;){
            nums1[m++] = nums2[b++];
        }
        Arrays.sort(nums1);
    }
}