from collections import deque

class FreqStack:

    def __init__(self):
        self.stack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> int:
        arr = []

        while self.stack:
            arr.append(self.stack.pop())

        max_freq = 0
        chosen_index = 0

        for i in range(len(arr)):
            freq = 0
            for j in range(len(arr)):
                if arr[j] == arr[i]:
                    freq += 1

            if freq > max_freq:
                max_freq = freq
                chosen_index = i

        ans = arr[chosen_index]

        for i in range(len(arr) - 1, -1, -1):
            if i == chosen_index:
                continue
            self.stack.append(arr[i])

        return ans


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
