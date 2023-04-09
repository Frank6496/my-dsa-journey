class Stack:
    def __init__(self) -> None:
        self.stack = []

    def __repr__(self) -> str:
        return str(self.stack)

    def size(self):
        return len(self.stack)
    
    def is_empty(self):
        return not self.stack # or len(self.stack) == 0
   
    def push(self, data):
        self.stack.append(data)

    def pop(self):
        self.stack.pop()
    
    def peek(self):
        return self.stack[-1]

    def reverse_str(self, strs):
        for char in range(len(strs) - 1, -1, -1):
            self.stack.append(strs[char])
        return self.stack
