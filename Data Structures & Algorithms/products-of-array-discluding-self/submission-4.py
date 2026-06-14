class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans= []
        n = len(nums)

        prefix = [1]*n
        #changes everything but the 1st element
        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        #changes everything but the last element
        suffix = [1]*n
        for i in range(n-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]

        for i in range(0,n):
           ans.append(prefix[i]*suffix[i])

        return ans