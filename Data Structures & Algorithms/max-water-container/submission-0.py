class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #create 2 pointers, one called left, one called right, and also a max variable
        left = 0
        right = len(heights)-1
        ans = 0
        sum = 0
        
        while left < right:
            #multiply lenghth of heights subarray by the min(heights[left],heights[right])
            sum = min(heights[left],heights[right])*(right-left)
            ans = max(sum,ans)
            #update one of the variables
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        #return max
        return ans

