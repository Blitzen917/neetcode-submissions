class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #sort the input array
        nums = sorted(nums)
        result = []
        #iterate through nums w/ index i and get -nums[i] = nums[j] + nums[k]
        for i in range(len(nums)):
            #skip i if the same as i-1
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            target = -nums[i]
            #calculate j and k pairs w/o duplicates
            #create 2 pointers, one left, one right
            j = i + 1
            k = len(nums) - 1

            while j<k:
                if nums[j] + nums[k] < target:
                    j+=1
                elif nums[j] + nums[k] > target:
                    k-=1
                else:
                    result.append([nums[i],nums[j],nums[k]])
                    j+=1
                    k-=1
                    #increment j
                    while j<k and nums[j] == nums[j-1]:
                        j+=1
                    #increment k
                    while j<k and nums[k] == nums[k+1]:
                        k-=1
        return result
