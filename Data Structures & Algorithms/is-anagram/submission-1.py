class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        shash = {}
        thash = {}
        for letter in s:
            if letter not in shash:
                shash[letter]=1
            else:
                shash[letter]+=1
        for letter in t:
            if letter not in thash:
                thash[letter]=1
            else:
                thash[letter]+=1
        if shash.items() == thash.items():
            return True
        else:
            return False
        