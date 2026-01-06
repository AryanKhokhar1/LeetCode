class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        answer = []
        for ele in nums:
            if ele < pivot:
                answer.append(ele)
        for ele in nums:
            if ele == pivot:
                answer.append(ele)
        for ele in nums:
            if ele > pivot:
                answer.append(ele)
        return answer