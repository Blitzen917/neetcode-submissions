class Solution:

    def encode(self, strs: List[str]) -> str:
        string = '';
        for word in strs:
            string+= str(len(word)) + '#' + word
        return string

    def decode(self, s: str) -> List[str]:
        strings = []
        start = 0
        while(start<len(s)):
            hashPointer = s.find('#', start)
            length = int(s[start:hashPointer])
            word = s[hashPointer+1:hashPointer+1+length]

            strings.append(word)
            start=(hashPointer+1+len(word))

        return strings

