class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0

        def binarySearch(arr):
            start = 0
            end = len(arr)-1
            while(start<=end):
                mid = start + (end - start) //2
                if arr[mid] >= 0:
                    start = mid + 1
                else:
                    end = mid -1
            if start == len(arr):
                return 0
            if end == -1:
                return len(arr)
            return len(arr) - start
        for arr in grid:
            count += binarySearch(arr)
        return count 