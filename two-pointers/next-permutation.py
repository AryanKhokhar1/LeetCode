class Solution(object):
    def nextPermutation(self, nums):
        result = []
        def permutation(plist, unlist):
            if (len(unlist)) == 0:
                result.append(plist)
                return
            for i in range(len(plist)+1):
                permutation(plist[0:i]+[unlist[0]]+plist[i:],unlist[1:])
        permutation([],nums)
        result = list(set(tuple(subtup) for subtup in result))
        result = [list(sublist) for sublist in result]
        result.sort()
        index = 0
        while(result[index] != nums):
            index += 1
        if(index == len(result)-1):
            nums[:] = result[0]
        else:
            nums[:] = result[index+1]