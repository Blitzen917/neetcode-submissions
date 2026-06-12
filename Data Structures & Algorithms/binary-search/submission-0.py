class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #initialize low and high
        low, high = 0, len(nums)-1
        #while low < high:
        while low<=high:
            #set mid = to (low+high)//2
            mid = int(low+high)//2
            #if nums[mid]<target:
            if nums[mid]<target:
                low = mid + 1
            #elif nums[mid]>target:
            elif nums[mid]>target:
                high = mid - 1
            #else 
            else:
                return mid
        return -1