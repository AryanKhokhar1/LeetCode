class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        curr = len(nums1)-1
        m -= 1
        n -= 1
        while n >= 0 and curr >= 0:
            if nums1[m] < nums2[n]:
                nums1[curr] = nums2[n]
                n -=1
            else:
                extra = nums1[curr]
                nums1[curr] = nums1[m]
                nums1[m] = extra
                m -=1
            curr -=1