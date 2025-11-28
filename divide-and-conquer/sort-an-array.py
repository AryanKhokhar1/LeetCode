class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.divide(nums)
    
    def divide(self,arr):
        if len(arr) == 1:
            return arr

        mid = len(arr)//2
        left = self.divide(arr[:mid])
        right = self.divide(arr[mid:])
        return self.merge(left,right)
    
    def merge(self,left,right):
        newarr = []

        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                newarr.append(left[i])
                i+=1
            else:
                newarr.append(right[j])
                j+=1
        while i<len(left):
            newarr.append(left[i])
            i += 1
        while j < len(right):
            newarr.append(right[j])
            j += 1
        return newarr