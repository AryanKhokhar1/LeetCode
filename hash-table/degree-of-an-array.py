class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = dict()
        maximum = [0,0]
        for ele in nums:
            if count.get(ele) is None:
                count[ele] = 1
                if count[ele] > maximum[1]:
                    maximum[0] = ele
                    maximum[1] = count[ele]
            else:
                count[ele] +=1
                if count[ele] > maximum[1]:
                    maximum[0] = ele
                    maximum[1] = count[ele]
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i] != maximum[0]:
                i += 1
            elif nums[j] != maximum[0]:
                j-=1
            else:
                break
        return j-i+1