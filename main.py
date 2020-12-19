class Element:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None

    def push(self, value):
        if self.top is None:
            self.top = Element(value)

        else:
            newelement = Element(value)
            newelement.next = self.top
            self.top = newelement

    def pop(self):
        if self.top.next is None:
            return None
        else:
            poppedelement = self.top
            self.top = self.top.next
            print(poppedelement.value)


c1 = Stack()
c1.push(11)
print(c1.top.value)
c1.push(22)
print(c1.top.value)
c1.pop()
