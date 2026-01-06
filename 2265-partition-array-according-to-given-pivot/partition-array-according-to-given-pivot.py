class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        small = []
        large = []
        equal = 0
        for ele in nums:
            if ele < pivot:
                small.append(ele)
            elif ele > pivot:
                large.append(ele)
            else:
                equal += 1
        return small + [pivot]*equal + large
