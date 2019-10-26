
import sys
class Stack:
    #
    #  Stack ADT has three methods: is_empty, push and pop.
    #
    def __init__(self,capacity = 10 ):
        self.stack = [0] * capacity
        self.top = 0

    def is_empty(self):
        return self.top == 0

    def push(self, item):
        if self.top < len(self.stack):
            self.stack[self.top] = item
        else:
            self.stack.append(item)

        self.top += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            self.top -= 1
            return self.stack[self.top]

    def maxim(self):
        return max(self.stack)


    def minimum(self):
        return min(self.stack)

    def reverse_line(self, data):
        S = Stack()
        line = data.split()
        for i in line:
            S.push(i)
        while   S.is_empty() :


            print(S.pop())


    def reverse_input(stack):
        text = sys.stdin.read().splitlines()
        line = text.pop()
        while line is not None:
            print(line)
            try:
                line = text.pop()
            except IndexError:
                break


s = Stack(10)
s.push(5)
s.push(6)
s.push(7)
s.push(19)
s.push(97)
s.push(102)
s.push(7)
s.push(101)
s.push(2)
s.push(7)
s.push(5)
s.push(5)
s.push(6)
s.push(7)
s.push(19)
s.push(97)
s.push(102)
s.push(7)
s.push(101)
s.push(2)
s.push(7)
s.push(5)
s.push(5)
s.push(6)
s.push(7)
s.push(19)
s.push(97)
s.push(102)
s.push(7)
s.push(101)
s.push(2)
s.push(7)
s.push(5)
s.push(5)
s.push(6)
s.push(7)
s.push(19)
s.push(97)
s.push(102)
s.push(7)
s.push(101)
s.push(2)



print(s.maxim())
print(s.minimum())
print(s.pop())
























