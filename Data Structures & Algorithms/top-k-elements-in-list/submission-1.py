class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        #get list of (key,value) pairs
        sortedHash = list(hash.items())
        #sort by the second element (frequency) in descending order
        sortedHash.sort(key=lambda x: x[1], reverse=True)
        #extrract the first k keys
        result = [item[0] for item in sortedHash[:k]]

        return result