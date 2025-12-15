class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        curr = 1
        n = 1
        prev = set()
        while curr % k:
            if curr in prev:
                return -1
            prev.add(curr)
            curr = 10*(curr %k) + 1
            n += 1
        return n