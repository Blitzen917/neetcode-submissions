class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maximumWater = 0
        while left < right:
            currentWater = min(heights[left],heights[right])*(right-left)
            maximumWater = max(maximumWater, currentWater)
            if heights[left] <= heights[right]:
                left+=1
            else:
                right-=1
        
        return maximumWater
            