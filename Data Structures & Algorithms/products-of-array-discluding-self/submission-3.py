class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroIndexes = []
        numZeroes = 0
        ans = []
        nonzeroProduct = 1

        for i,num in enumerate(nums):
            if num == 0:
                numZeroes += 1
                zeroIndexes.append(i)
            else:
                nonzeroProduct *= num
        
        if numZeroes == 1:
            ans = [0]*len(nums)
            ans[zeroIndexes[0]] = nonzeroProduct
            return ans
        
        if numZeroes >= 2:
            return [0]*len(nums)
        
        for num in nums:
            ans.append(int(nonzeroProduct/num))
        return ans