class Solution(object):
    def combinationsumhelp(self,start,currentCandidates, candidates, target, answer):
        if(sum(currentCandidates)== target):
            answer.append(currentCandidates[:])
            # print(currentCandidates)
            return
        for i in range(start,len(candidates)):
            num = candidates[i]
            if(sum(currentCandidates)+num <= target):
                currentCandidates.append(num)

                self.combinationsumhelp(i,currentCandidates, candidates, target, answer)

                currentCandidates.pop(-1)
    def combinationSum(self, candidates, target):
        answer = []
        self.combinationsumhelp(0,[],candidates, target,answer)
        return answer
        
        