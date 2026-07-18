class MinStack:


    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        #if empty or the value is less than the top value of minStack
        #add it to the top of minStack
        if not self.minStack or self.minStack[-1] > val:
            self.minStack.append(val)
        #else repeat the top value
        else:
            self.minStack.append(self.minStack[-1])

        print(self.minStack)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
        
