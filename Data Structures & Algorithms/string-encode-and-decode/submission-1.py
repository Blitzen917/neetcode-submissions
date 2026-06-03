class Solution:
    #"5#apple"
    def encode(self, strs: List[str]) -> str:
        ans = ""
        for string in strs:
            ans+=(str(len(string))+'#'+string)
        return ans
    def decode(self, s: str) -> List[str]:
        ans = []
        #declare bookmark pointer
        bookmark = 0
        while bookmark < len(s):
            #dsearch for first #, starting at bookmark
            hashPosition = s.find('#',bookmark)
            #length is everything left of #
            length = int(s[bookmark:hashPosition])
            #string is <length> to the right of bookmark pointer
            string = s[hashPosition+1:hashPosition+1+length]
            #add string to ans list
            ans.append(string)
            #update bookmark
            bookmark = hashPosition + 1 + length
        return ans

