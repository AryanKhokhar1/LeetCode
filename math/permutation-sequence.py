class Solution(object):
    def getPermutation(self, n, k):
        per = []
        
        def perm(pstr, unstr):
            if len(unstr) == 0:
                per.append(pstr)
                return
            
            for i in range(len(pstr)+1):
                perm(pstr[0:i] + unstr[0]+ pstr[i:], unstr[1:])
        s = ""
        for i in range(1,n+1):
            s = s + str(i)
        perm("",s)
        per.sort()
        return per[k-1]
