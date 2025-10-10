class NumArray:
    
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefixnums = []

        total = 0
        for ele in nums:
            total += ele
            self.prefixnums.append(total)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixnums[right]
        else:
            return self.prefixnums[right] - self.prefixnums[left -1]
