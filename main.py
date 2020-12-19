class Element:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class Stack:

    def __init__(self):
        self.top = None

    def push(self, key, value):
        if self.top is None:
            self.top = Element(key, value)
        elif self.top.key < key:
            self.top = Element(key, value)

    def printout(self):
        print(self.top.key, self.top.value)


c1 = Stack()
print('Input key')
a = int(input())
print('Input value')
b = int(input())
c1.push(a, b)
c1.printout()
