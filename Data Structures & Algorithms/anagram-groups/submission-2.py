class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) < 2:
            return [strs]
        else:
            ans = {}
            for word in strs:
                sortedWord = ''.join(sorted(word)) #sorted returns a list of characters
                print(sortedWord)
                if sortedWord in ans.keys():
                    ans[sortedWord].append(word)
                else:
                    ans[sortedWord] = [word]
        print(ans.values())
        return list(ans.values())