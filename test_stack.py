# list 
l = []
l.append(1)
l.append(2)

print(l)  # Output: [1, 2]
l.pop()
print(l)  # Output: [1]

## stack
def spush(stack, item):
    stack.append(item)

def spop(stack):
    return stack.pop()  


stack = []

spush(stack, 1) 
spush(stack, 2)

print(stack)  # Output: [1, 2]

print(spop(stack))  # Output: 2
print(stack)  # Output: [1]
