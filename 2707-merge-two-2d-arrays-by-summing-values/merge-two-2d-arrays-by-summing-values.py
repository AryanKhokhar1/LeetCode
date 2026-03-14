class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i , j = 0 , 0
        lnum1 = len(nums1)
        lnum2 = len(nums2)
        output = []
        while i < lnum1 and j < lnum2:
            if nums1[i][0] == nums2[j][0]:
                output.append([nums1[i][0],nums1[i][1] + nums2[j][1]])
                i+=1
                j+=1
            elif nums1[i][0] < nums2[j][0]:
                output.append([nums1[i][0],nums1[i][1]])
                i+=1
            else:
                output.append([nums2[j][0], nums2[j][1]])
                j+=1
        
        while i < lnum1:
            output.append(nums1[i])
            i+=1
        while j < lnum2:
            output.append(nums2[j])
            j+=1
        return output