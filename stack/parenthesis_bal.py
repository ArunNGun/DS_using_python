from stack import Stack

input =input("enter the parenthesis")
stack=Stack()
for i in range(len(input)):
    if input[i] in "{[(":
        stack.push(input[i])

    elif input[i] in ")}]":
        
        stack.pop()
    else:
        continue
if stack.is_empty():
    print("balanced")
else:
    print("unbalanced")
