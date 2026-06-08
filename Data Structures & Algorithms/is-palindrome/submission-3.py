class Solution:
    def isPalindrome(self, s: str) -> bool:
        #set 2 pointers, one at the left end and one at the right end
        left = 0
        right = len(s) - 1
        #create a while loop where the conditions is while left < right
        while left<right:
            #check if left and right are at characters that are alphanumeric
            if s[left].isalnum() == False:
                left+=1
                continue
            if s[right].isalnum() == False:
                right-=1
                continue
            #return false if at any moment s[left]!=s[right]
            if s[left].lower()!=s[right].lower():
                return False
            #update pointers at the end of loop
            left+=1
            right-=1
        #otherwise return true outside the while loop
        return True