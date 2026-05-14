class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashNums = {}
        difference = 0
        for i,num in enumerate(nums):
            difference = target - nums[i]
            if difference in hashNums.values():
                j = nums.index(difference)
                return [i,j] if i<j else [j,i]
            else:
                hashNums[i] = num


        

        