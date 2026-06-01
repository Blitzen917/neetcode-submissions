class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}

        for i in range(len(nums)):
            difference = target - nums[i]
            if nums[i] in found:
                j = found[nums[i]]
                return [i,j] if i<j else [j,i]
            else:
                found[difference] = i