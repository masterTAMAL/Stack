class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class StackLinkedList:
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        removed = self.top
        self.top = self.top.next
        return removed.data

    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None

    def traverse(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            temp = self.top
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
        print()


s = StackLinkedList()

s.push(1)
s.push(2)
s.push(3)

s.traverse()      # 3 2 1 (Top to Bottom)

print("Popped:", s.pop())   # 3

s.traverse()      # 2 1
