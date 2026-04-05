class Queue:
    def __init__(self):
        self.items = []

    def push_q(self, item):
        self.items.append(item)

    def pop_q(self):
        if self.is_empty_q():
            return None
        return self.items.pop(0)

    def peek_q(self):
        if self.is_empty_q():
            return None
        return self.items[0]

    def size_q(self):
        return len(self.items)

    def is_empty_q(self):
        return len(self.items) == 0

class MyStack:

    def __init__(self):
        self.queue = Queue()

    def push(self, x: int) -> None:
        self.queue.push_q(x)
        for _ in range(self.queue.size_q() - 1):
            self.queue.push_q(self.queue.pop_q())

    def pop(self) -> int:
        return self.queue.pop_q()

    def top(self) -> int:
        return self.queue.peek_q()

    def empty(self) -> bool:
        return self.queue.is_empty_q()
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
