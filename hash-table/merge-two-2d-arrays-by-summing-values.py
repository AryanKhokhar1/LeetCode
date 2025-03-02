class Solution(object):
    def mergeArrays(self, nums1, nums2):
        i = 0
        j = 0
        nums = []
        while(i < len(nums1) and j < len(nums2)):
            if nums1[i][0] == nums2[j][0]:
                nums.append([nums1[i][0],nums1[i][1]+nums2[i][1]])
                i += 1
                j += 1
            elif nums1[i][0] > nums2[j][0]:
                nums.append(nums2[j])
                j += 1
            else:
                nums.append(nums1[i])
                i+=1
        while i<len(nums1):
            nums.append(nums1[i])
            i+=1
        while j<len(nums2):
            nums.append(nums2[j])
            j+=1
        return nums

