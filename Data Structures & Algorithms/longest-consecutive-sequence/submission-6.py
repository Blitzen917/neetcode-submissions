class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        #sort from least to greatest
        nums=sorted(nums)
        #create list to remember longest sequence so far
        longestSequence = []
        currentSequence = []
        for num in nums:
            if len(currentSequence) == 0:
                currentSequence.append(num)
                # updates longestSequence for single element case
                if len(currentSequence) > len(longestSequence):
                    longestSequence = currentSequence
                continue
            #skips current num
            if currentSequence[-1] == num:
                continue
            else:
                #sequence is continued
                if num == currentSequence[-1] + 1:
                    currentSequence.append(num)
                #sequence is broken
                if num > currentSequence[-1] + 1:
                    if len(currentSequence) > len(longestSequence):
                        longestSequence = currentSequence
                    currentSequence = [num]
            
            #updates longestSequence
            if len(currentSequence) > len(longestSequence):
                longestSequence = currentSequence
        
        #return length of longestSequence

        return len(longestSequence)
        