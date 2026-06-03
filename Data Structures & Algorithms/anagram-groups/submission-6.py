class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        if len(strs)<2:
            return [strs]
        strDict = defaultdict(list)
        for string in strs:
            letters = [0]*26
            for c in string:
                letters[ord(c)-ord('a')]+=1
            strDict[tuple(letters)].append(string)
        return list(strDict.values())
        

