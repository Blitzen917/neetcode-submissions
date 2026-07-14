class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, end = 0, 0
        longest = 0
        count = defaultdict(int)
        
        if end<=len(s):
            count[s[end]]+=1

        while end<len(s):
            #expand 
            if end - start + 1 -max(count.values()) <= k:
                longest = max(longest, end-start+1)
                end+=1
                if end < len(s):
                    count[s[end]]+=1
            #reduce window size
            else:
                while end - start + 1 -max(count.values()) > k:
                    count[s[start]]-=1
                    start+=1
                
                if end - start + 1 -max(count.values()) <= k:
                    longest = max(longest, end-start+1)
                    end+=1
                    if end < len(s):
                        count[s[end]]+=1
            
        return longest
               

           