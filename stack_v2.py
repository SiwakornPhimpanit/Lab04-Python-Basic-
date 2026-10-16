class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.items:
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.items:
            raise IndexError("peek from empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)
        
s = Stack()
s.push("Hello, World!")
s.push("This is a test.")
print(s.pop())  # Output: This is a test.


m = Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
print(m.peek())


m = Stack()
m.push('x')
m.push('y')
m.push('z')
while not m.is_empty():
    print(m.pop())
    print(m.pop())