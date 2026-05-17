class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ''' answer = defaultdict(list)
        for string in strs:
            key = ''.join(sorted(string)) #correct way to sort a string
            answer[key].append(string) 
        return list(answer.values()) '''

        answer = defaultdict(list) #lets the dict has lists for values

        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1 #adds count to c letter
            answer[tuple(count)].append(string)
        return list(answer.values())
