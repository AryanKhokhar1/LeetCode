class Solution(object):
    def xorOfList(self, lis):
        if lis is None or len(lis) == 0:
            return 0
        ans = lis[0]
        for i in range(1, len(lis)):
            ans = ans ^ lis[i]
        return ans

    def subsetXORSum(self, nums):
        self.answer = 0
        def subSET(templis,index):
            if len(nums) == index:
                self.answer += self.xorOfList(templis)
                return 
            
            subSET(templis,index+1)

            templis.append(nums[index])
            subSET(templis,index+1)
                

        subSET([],0)
        return self.answer