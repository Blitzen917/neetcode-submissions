class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        #loop through nums (#add plus 1 to each hashmap[num] such that it keeps track of frequency)
        for num in nums:
            if num not in hashmap.keys():
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        #sort hashmap by frequencies
        sortedHashmap = sorted(hashmap.items(), key=lambda item: item[1], reverse=True) #inside it now looks like (number, frequency)
        answer = []
        for i in range (k):
            answer.append(sortedHashmap[i][0]) #looks at the kth tuple, and grabs the key
        return answer
