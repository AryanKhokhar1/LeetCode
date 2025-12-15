class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        d = Counter(arr)
        val = list(d.values())
        val.sort()
        answer = 0
        total = 0
        i = len(val) -1
        half = len(arr) // 2
        while i >= 0 and total < half:
            total += val[i]
            i -= 1
            answer += 1
        return answer