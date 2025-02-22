class Solution(object):
    def trap(self, height):
        n = len(height)
        if n == 0:
            return 0

        left = [0]*len(height)
        right = [0]*len(height)

        # Left to Right maximum
        left[0] = height[0]
        for i in range(1,len(height)):
            left[i] = max(left[i-1], height[i])

        # Right to Left Maximum
        right[-1] = height[-1]
        for i in reversed(range(len(height)-1)):
            right[i] = max(right[i+1],height[i])
        
        tapWater = 0
        for i in range(len(height)):
            tapWater += min(left[i] ,right[i]) - height[i]
        return tapWater