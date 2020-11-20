class Num:
    def __init__(self, x):
        self.x = x

    def check(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        if self.a+self.b+self.c == self.x:
            print('Correct')
        else:
            print('Incorrect')


print('Input Num A')
a = int(input())
print('Input Num B')
b = int(input())
print('Input Num C')
c = int(input())

print('Input num X')
x = int(input())

f = Num(x)
f.check(a, b, c)
