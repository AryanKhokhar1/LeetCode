class Solution(object):
    def lcm(self, num1, num2):
        return (num1 * num2)/self.findgcd(num1, num2)
    def findgcd(self,num1, num2):
        if num2 == 0:
            return num1
        num1, num2 = num2, num1%num2
        return self.findgcd(num1,num2)
    def replaceNonCoprimes(self, nums):
        stack = [nums[0]]
        if len(nums) < 2:
            return nums
        i = 1
        isCop = True
        while i < len(nums):
            if isCop or len(stack) == 1:
                stack.append(nums[i])
                i += 1
            lcmVal = int(self.lcm(stack[-1],stack[-2]))
            if (lcmVal != stack[-1]*stack[-2]):
                stack.pop()
                stack.pop()
                stack.append(lcmVal)
                isCop = False
            else:
                isCop = True
        return stack