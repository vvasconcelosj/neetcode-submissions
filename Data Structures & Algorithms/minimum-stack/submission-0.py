class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        currentMin = val
        if self.stack:
            currentMin = min(currentMin, self.getMin())

        self.stack.append((val, currentMin))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0]

    def getMin(self) -> int:
        return self.stack[-1][1]
        
