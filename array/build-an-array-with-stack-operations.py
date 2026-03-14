class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        a = 0
        for i in range(1,n+1):
            if target[a] == i:
                ans.append("Push")
                if a == len(target)-1:
                    break
                a+=1
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans