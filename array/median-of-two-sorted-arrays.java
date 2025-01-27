class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        
        int[] allnum = new int[nums1.length + nums2.length];
        int a = 0;
        int b= 0;
        for(int i = 0; i<allnum.length; i++){
            if(a<nums1.length && b <nums2.length){
                if(nums1[a] < nums2[b]){
                    allnum[i] = nums1[a++];
                }else{
                    allnum[i] = nums2[b++];
                }
            }else{
                if(a<nums1.length){
                    allnum[i] = nums1[a++];
                }else if(b<nums2.length){
                    allnum[i] = nums2[b++];
                }
            }
        }
        // System.out.println(Arrays.toString(allnum));
        if(allnum.length %2 == 0 && allnum.length>0){
            return (allnum[allnum.length/2] +allnum[(allnum.length/2)-1])/2f;
        }
        return allnum[allnum.length/2];
    }
}