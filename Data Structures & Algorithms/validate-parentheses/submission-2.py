class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for letter in s:
            if letter == "(" or letter == "[" or letter == "{":
                stack.append(letter)
            elif letter == ")":
                if not stack or stack[-1] != "(":
                    return False
                stack.pop()
            elif letter == "]":
                if not stack or stack[-1] != "[":
                    return False
                stack.pop()
            elif letter == "}":
                if not stack or stack[-1] != "{":
                    return False
                stack.pop()
            print(stack)
        
        return not stack