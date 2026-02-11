class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size   # fixed size array
        self.top = -1

    def push(self, value):
        if self.top == self.size - 1:
            print("Overflow")
        else:
            self.top += 1
            self.stack[self.top] = value

    def pop(self):
        if self.top == -1:
            print("Underflow")
        else:
            data = self.stack[self.top]
            self.top -= 1
            return data

    def traverse(self):
        if self.top == -1:
            print("Stack is Empty")
        else:
            for i in range(self.top + 1):
                print(self.stack[i], end=" ")
        print()

s = Stack(3)

s.push(1)
s.push(2)
s.push(3)

s.traverse()   # 1 2 3

print("Popped:", s.pop())  # 3

s.traverse()   # 1 2
