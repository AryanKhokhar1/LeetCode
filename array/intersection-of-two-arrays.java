class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        ArrayList<Integer> answer = new ArrayList<>();
        for(int a = 0, b= 0; a< nums1.length && b < nums2.length;){
            if(nums1[a] == nums2[b]){
                answer.add(nums1[a]);
                a++;
                b++;
            } else if(nums1[a] < nums2[b]){
                a++;
            }else if (nums1[a] > nums2[b]){
                b++;
            }
        }
        HashSet<Integer> set = new HashSet<>(answer);
        int[] ans = new int[set.size()];
        int i = 0;
        for(int ele:set){
            ans[i] = ele;
            i++;
        }
        return ans;
    }
}