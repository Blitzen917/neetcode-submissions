class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            if char in ('(','[', '{'):
                stack.append(char)
            else:
                print(stack)
                if len(stack) == 0:
                    return False

                if char == ')' and stack[-1] == '(':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    return False

        return True if len(stack) == 0 else False