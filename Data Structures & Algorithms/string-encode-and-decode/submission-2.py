class Solution:

    def encode(self, strs: List[str]) -> str:
        #going to encode each string to be ex: 5#apple
        ans = ''
        for string in strs:
            ans= ans + str(len(string)) + '#' + string
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        start = 0
        hashPointer = 0
        while start<len(s):
            hashPointer = s.find('#', start) #set hashPointer to location of first #
            num = int(s[start:hashPointer]) #set num = int(s[start:hashPointer])
            word = s[hashPointer+1:hashPointer+1+num] #set word = s[hashPointer+1:hashPointer+1+num]
            ans.append(word) #ans.append(word)

            start = hashPointer+1+num #start = hashPointer+1+num #update start pointer
        
        return ans
