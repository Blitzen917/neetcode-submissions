class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        mid = 0

        while low<=high:
            mid = int(low+high)//2
            if nums[mid] == target:
                return mid
            if nums[low]<=nums[mid]:    #left half is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return mid if nums[mid] == target else -1