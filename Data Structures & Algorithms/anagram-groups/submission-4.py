class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for word in strs:
            sortedWord = ''.join(sorted(word)) #sorted returns a list of characters
            print(sortedWord)
            ans[sortedWord].append(word)
        return list(ans.values())