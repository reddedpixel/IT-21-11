class Num:
    def __init__(self, x):
        self.x = x

    def check(self, a, b, c):
        if a + b + c == self.x:
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
