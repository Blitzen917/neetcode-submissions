class Solution:

    def encode(self, strs: List[str]) -> str:
        #could encode stuff as 5#Hello, 5#Hello, 5#Hello...
        res = ''
        for string in strs:
            encodedString = str(len(string))+'#'+string
            res+=encodedString
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        front = 0 #where the num of a word starts
        while front < len(s): 
            hashtagLocation = s.index('#',front)
            #extract number before hashtag
            num = int(s[front:hashtagLocation])
            #use that num to know how many chars to grab after #
            string = s[hashtagLocation+1:hashtagLocation+1+num]
            #add string to result list
            res.append(string)
            #move front pointer forward
            front = hashtagLocation+1+num

        return res
