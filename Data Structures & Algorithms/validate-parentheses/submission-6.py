class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:

            #if ( { or [, add to stack
            if char in ('(','{','['):
                stack.append(char)
            #if } ] ), check if their opposite is at the top of stack
            else:
                if stack:
                    if char == ')':
                        if stack[-1] == '(':
                            stack.pop()
                        else:
                            return False
                    elif char == ']':
                        if stack[-1] == '[':
                            stack.pop()
                        else:
                            return False
                    elif char == '}':
                        if stack[-1] == '{':
                            stack.pop()
                        else:
                            return False
                else:
                    return False
        
        #return true
        if not stack:
            return True
        else:
            return False