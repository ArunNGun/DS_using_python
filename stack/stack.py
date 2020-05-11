#!usr/bin/python3

class Stack():
    def __init__(self):
        self.stack = []

    def push(self,data):
        self.stack.append(data)
        return True
    def pop(self):
        value=self.stack[-1]
        del(self.stack[-1])
        return value
    def is_empty(self):
        return self.stack == []
    def printstack(self):
        return print(self.stack)
    def peek(self):
        if not self.is_empty():
            return print(self.stack[-1])
        else:
            return print("stack is empty")
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
