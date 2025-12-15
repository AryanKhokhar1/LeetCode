class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        d1 = dict()
        setarr2 = set(arr2)
        lastanswer = []
        for ele in arr1:
            if ele not in setarr2:
                lastanswer.append(ele)
            else:
                if d1.get(ele) == None:
                    d1[ele] = 1
                else:
                    d1[ele] += 1
        new_lis = []
        for ele in arr2:
            new_lis.extend([ele]*d1.get(ele))
        lastanswer.sort()
        return new_lis + lastanswer