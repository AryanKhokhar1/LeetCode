class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        i = 0
        j = 1 
        k = 2
        maxvalue = (nums[i] - nums[j])*nums[k]

        while i <= len(nums)-3:
            maxvalue = max(maxvalue, (nums[i] - nums[j])*nums[k])
            if k < len(nums)-1:
                k += 1
            else:
                if j < len(nums)-2:
                    j+=1
                    k = j+1
                else:
                    i += 1
                    j = i+1
                    k = j + 1
        if maxvalue < 0:
            return 0
        else:
            return maxvalue
