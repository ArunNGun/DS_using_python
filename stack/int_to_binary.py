#!usr/bin/python3
from stack import Stack

value = input("enter the integer value")
stack=Stack()

while value!=0:
    remainder=int(value)%2
    value=int(value)/2
    if value ==1:
        stack.push(str(value))
        break
    stack.push(str(remainder))
result=""
while not stack.is_empty():
    result+=str(stack.pop())

print(result)
