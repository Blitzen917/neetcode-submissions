class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums=sorted(nums) #sort the array
        ans = []
        for i, num in enumerate(nums):
            if i>0 and num == nums[i-1]:
                continue
            
            j, k = i+1, len(nums)-1

            while j<k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < 0:
                    j+=1
                elif sum > 0:
                    k-=1
                else:
                    ans.append((nums[i],nums[j],nums[k]))
                    while j<k and nums[j]==nums[j+1]:
                        j+=1
                    while j<k and nums[k]==nums[k-1]:
                        k-=1
                    j += 1
                    k -= 1
        
        return ans
            
