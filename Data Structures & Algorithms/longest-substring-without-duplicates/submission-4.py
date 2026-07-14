class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        longest = 0
        while end<len(s):
            string = s[start:end]

            if s[end] not in string:
                end+=1
            else:
                start+=1

            longest = max(longest, len(s[start:end]))

        return longest