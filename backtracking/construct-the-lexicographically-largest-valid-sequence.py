class Solution(object):
    def constructDistancedSequence(self, n):
        lis = [0]*(2*n -1)
        used = set()
        def backtrack(i):
            if(i == len(lis)):
                return True

            if lis[i] != 0:
                return backtrack(i+1)

            for num in reversed(range(1,n+1)):
                
                if num in used:
                    continue
                if num>1 and (num+i >= len(lis) or lis[num+i] != 0):
                    continue
                

                used.add(num)
                lis[i] = num
                if num > 1:
                    lis[i+num] = num

                if backtrack(i+1):
                    return True

                used.remove(num)
                lis[i] = 0
                if num > 1:
                    lis[i+num] = 0
            return False

        backtrack(0)
        return lis