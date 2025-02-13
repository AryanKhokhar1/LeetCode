class Solution(object):
    def combinationsumhelp(self,start,currentCandidates, candidates, target):
        if(sum(currentCandidates)== target):
            return [currentCandidates[:]]

        result = []
        for i in range(start,len(candidates)):
            num = candidates[i]
            if(sum(currentCandidates)+num <= target):
                currentCandidates.append(num)

                result.extend(self.combinationsumhelp(i,currentCandidates, candidates, target))

                currentCandidates.pop(-1)
        return result
    def combinationSum(self, candidates, target):
        
        return self.combinationsumhelp(0,[],candidates, target)        
        