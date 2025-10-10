class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefixnum = []
        total = 0
        for ele in nums:
            total += ele
            prefixnum.append(total)

        left = 0
        right = prefixnum[-1]
        for i in range(len(nums)):
            if i == 0:
                left = 0
                right = prefixnum[-1] - prefixnum[i]
            elif i == len(nums)-1:
                right = 0
                left = prefixnum[i-1]
            else:
                left = prefixnum[i-1]
                right = prefixnum[-1] - prefixnum[i]
            if left == right:
                return i
        return -1