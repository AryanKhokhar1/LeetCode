class Solution(object):
    def lcm(self, num1, num2):
        return (num1 * num2)/self.findgcd(num1, num2)
    def findgcd(self,num1, num2):
        if num2 == 0:
            return num1
        num1, num2 = num2, num1%num2
        return self.findgcd(num1,num2)
    def replaceNonCoprimes(self, nums):
        stack = nums[:]
        answer = []
        while len(stack) > 1:
            a = stack.pop(0)
            b = stack.pop(0)
            val = int(self.lcm(a,b))
            if val != a*b:
                stack.insert(0,val)
            else:
                answer.append(a)
                stack.insert(0,b)
        answer.append(stack.pop())
        return answer