class Solution:
    def smallestTrimmedNumbers(self, nums: List[str], queries: List[List[int]]) -> List[int]:
        ndigit = {x[1] for x in queries}
        ndigit = max(ndigit)
        inums = [[int(value),index] for index,value in enumerate(nums)]
        answer = [0]*len(queries)
        for n in range(ndigit):
            bucket = [[] for _ in range(10)]

            for i in range(len(nums)):
                foucsdigit = (inums[i][0]//(10**n))%10
                bucket[foucsdigit].append(inums[i])
            
            sorted_list = []
            for b in bucket:
                sorted_list.extend(b)
            inums = sorted_list

            for i in range(len(queries)):
                if queries[i][1] == n +1:
                    answer[i] = inums[queries[i][0]-1][1]
        return answer