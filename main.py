class Element:

    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:

    def __init__(self):
        self.top = None
        self.stsize = 0

    def push(self, value):
        self.stsize = self.stsize + 1
        if self.top is None:
            self.top = Element(value)

        else:
            newelement = Element(value)
            newelement.next = self.top
            self.top = newelement

    def pop(self):
        if self.top is None:
            return None
        else:
            self.stsize = self.stsize - 1
            poppedelement = self.top
            self.top = self.top.next
            return poppedelement.value

    def peek(self):
        if self.top is None:
            return None
        else:
            return self.top.value

    def size(self):
        return self.stsize

    def clear(self):
        self.top = None
        self.stsize = 0
