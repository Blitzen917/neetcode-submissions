class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #brute for method would be to create a dict, count freq using dict, sort array by freq, then select top k elements

        hash = dict()
        setNums = set(nums)
        for num in nums:
            if num not in hash:
                hash[num] = 1
            else:
                hash[num]+=1
        
        #bucket sort
        buckets = [[] for _ in range(len(nums)+1)]

        for num in setNums:
            buckets[hash[num]].append(num)

        ans = []
        while len(ans) < k:
            for i in range(len(buckets)-1, 0, -1):
                for element in buckets[i]:
                    ans.append(element)
                    if(len(ans)==k):
                        return ans
        return ans