class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        #count frequencies
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        ''' #get list of (key,value) pairs
        sortedHash = list(hash.items())
        #sort by the second element (frequency) in descending order
        sortedHash.sort(key=lambda x: x[1], reverse=True)
        #extrract the first k keys
        result = [item[0] for item in sortedHash[:k]] '''

        #reverse bucket sort
        freq = [[] for _ in range(len(nums)+1)]
        for key, count in hash.items():
            freq[count].append(key)
        
        result = []

        #get k freq elements
        for i in range(len(freq)-1, 0, -1):
            for element in freq[i]:
                result.append(element)
                if len(result) == k:
                    return result

        return result