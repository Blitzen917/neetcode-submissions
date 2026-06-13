class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        longestSeq, currentSeq = 0, 0
        newNum = 0

        for num in setNums:
            currentSeq = 1
            newNum = num
            while newNum+1 in setNums:
                currentSeq+=1
                newNum+=1
            longestSeq = max(longestSeq,currentSeq)
        return longestSeq

