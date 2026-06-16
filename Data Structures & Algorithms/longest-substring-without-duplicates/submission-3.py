class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        longestSubstring = 0

        for k in range(n, 0, -1):
            for i in range(n-k+1):
                substring = s[i:i+k]

                if len(set(substring))==len(substring): #if unique characters == total characters, all chars are distinct
                    longestSubstring=max(longestSubstring,len(substring))
        
        return longestSubstring
                
