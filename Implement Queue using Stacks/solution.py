class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek_s(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

class MyQueue:

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x: int) -> None:
        self.s1.push(x)

    def pop(self) -> int:
        if self.s2.is_empty():
            while self.s1.is_empty() == False:
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self) -> int:
        if self.s2.is_empty():
            while self.s1.is_empty() == False:
                self.s2.push(self.s1.pop())
        return self.s2.peek_s()

    def empty(self) -> bool:
        return self.s1.is_empty() and self.s2.is_empty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
