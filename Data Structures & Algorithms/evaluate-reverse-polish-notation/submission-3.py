class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for character in tokens:
            match character:
                case "+":
                    firstNum = secondNum = 0
                    secondNum = stack[-1] #because second num got added after => on top
                    stack.pop()
                    firstNum = stack[-1]
                    stack.pop()
                    stack.append(firstNum + secondNum)
                case "-":
                    firstNum = secondNum = 0
                    secondNum = stack[-1] #because second num got added after => on top
                    stack.pop()
                    firstNum = stack[-1]
                    stack.pop()
                    stack.append(firstNum - secondNum)
                case "*":
                    firstNum = secondNum = 0
                    secondNum = stack[-1] #because second num got added after => on top
                    stack.pop()
                    firstNum = stack[-1]
                    stack.pop()
                    stack.append(firstNum * secondNum)
                case "/":
                    firstNum = secondNum = 0
                    secondNum = stack[-1] #because second num got added after => on top
                    stack.pop()
                    firstNum = stack[-1]
                    stack.pop()
                    stack.append(int(firstNum / secondNum)) #truncate towards zero, returning int
                case _:
                    stack.append(int(character))
        
        return stack[0]