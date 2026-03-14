class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        curr = m
        for ele in nums2:
            for i in range(curr,-1,-1):
                print(nums1, )
                if ele <= nums1[i-1]:
                    nums1[i] , nums1[i-1] = nums1[i-1], nums1[i]
                else: 
                    nums1[i] = ele
                    curr +=1
                    break
        