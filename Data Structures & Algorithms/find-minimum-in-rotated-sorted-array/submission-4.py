class Solution:
    def findMin(self, nums: List[int]) -> int:
        #define low and high
        low, high = 0, len(nums)-1
        while low<high:
            mid = int(low+high)//2
            if nums[mid]<nums[high]:
                high = mid
            else:
                low = mid + 1
        return nums[low] #could've returned nums[high] if we wanted too
