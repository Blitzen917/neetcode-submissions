class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)
        for i,num in enumerate(nums):
            for j,spot in enumerate(res):
                if i!=j:
                    res[j]*=num
        return res

