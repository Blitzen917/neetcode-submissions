class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<2:
            return [strs]
        
        hash = defaultdict(list)

        for word in strs:
            wordDict = [0]*26
            for char in word:
                wordDict[ord(char)-ord('a')]+=1
            hash[tuple(wordDict)].append(word)

        return list(hash.values())