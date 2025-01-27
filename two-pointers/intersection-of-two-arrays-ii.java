class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        List<Integer> answer = new ArrayList<>();
        Arrays.sort(nums1);
        Arrays.sort(nums2);

        for(int i = 0, j = 0; i<nums1.length && j < nums2.length;){
            if(nums1[i] > nums2[j]){
                j++;
            }else if(nums2[j] > nums1[i]){
                i++;
            }else if(nums1[i] == nums2[j]){
                answer.add(nums1[i]);
                i++;
                j++;
            }
        }
        int[] ans = new int[answer.size()];
        int i = 0;
        for(int ele: answer){
            ans[i++] = ele;
        }
        return ans;
    }
}