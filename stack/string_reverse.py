from stack import Stack

str1="Hello"
revstr=""
stack=Stack()
i=0
for i in range(len(str1)):
    stack.push(str1[i])

for i in range(len(str1)):
    revstr+=stack.pop()

print(revstr)
