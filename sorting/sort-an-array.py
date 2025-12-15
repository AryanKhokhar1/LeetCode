class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if not nums:
            return nums
        
        neg = [-x for x in nums if x < 0]
        pos = [x for x in nums if x >= 0]

        neg = self.radixsort(neg)
        pos = self.radixsort(pos)

        neg = [-x for x in neg]
        neg = list(reversed(neg))
        return neg+pos
    def radixsort(self,lis):
        if not lis:
            return lis
        max_element = max(lis)
        ndigit = len(str(max_element))

        for n in range(ndigit):
            bucket = [[],[],[],[],[],[],[],[],[],[]]
            for ele in lis:
                focusdigit = (ele//(10**n))%10
                bucket[focusdigit].append(ele)
            
            new_lis = []
            for b in bucket:
                new_lis.extend(b)
            lis = new_lis
        return lis