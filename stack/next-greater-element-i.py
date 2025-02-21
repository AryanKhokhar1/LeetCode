class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        result = [-1]*len(nums2)
        stack = []
        for i in range(len(nums2)):
            while len(stack) > 0 and nums2[stack[-1]] < nums2[i]:
                index = stack.pop()
                result[index] = nums2[i]
            stack.append(i)
        ans = []
        print(result)
        for ele in nums1:
            ans.append(result[nums2.index(ele)])
        return ans