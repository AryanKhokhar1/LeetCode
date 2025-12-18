class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        answer = 0
        for ele in strs:
            if ele.isnumeric():
                answer = max(answer, int(ele))
            else:
                answer = max(answer, len(ele))

        return answer