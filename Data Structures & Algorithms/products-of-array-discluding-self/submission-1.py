class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #traverse array: count zeroes and multiply non zero numbers to prod
        prod = 1
        zeroCount = 0
        for num in nums:
            if num == 0:
                zeroCount+=1
            else:
                prod*=num
        #if zeroCount>1, return array of zeroes
        if zeroCount > 1:
            return [0] * len(nums)
        #create res array
        res = []
        #traverse array.
        for num in nums: 
            if zeroCount == 1:
                if num == 0:
                    res.append(prod)
                else:
                    res.append(0)
            else:
                res.append(prod // num)
        return res