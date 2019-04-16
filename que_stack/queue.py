from collections import deque
class Stack:
    def __init__(self):
        self.items = deque()

    def push(self,val):
        return self.items.append(val)

    def pop(self):
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0

    def top(self):
        return self.items[-1]

class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.s_in = Stack()
        self.s_out = Stack()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.s_in.push(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.s_out.empty():
            while not self.s_in.empty():
                self.s_out.push(self.s_in.pop())
        else:
            return self.s_out.pop()

        return self.s_out.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.s_out.empty():
            while not self.s_in.empty():
                self.s_out.push(self.s_in.pop())
        else:
            return self.s_out.top()

        return self.s_out.top()
                

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.s_in.empty() and self.s_out.empty()
