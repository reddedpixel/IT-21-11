
#print ('Input Num A')
#a = int(input())
#print ('Input Num B')
#b = int(input())
#print ('Input Num C')
#c = int(input())
#
#if a+b+c == 180:
#    print ('Triangle exists.')
#else:
#    print ('Triangle does not exist.')


class Num:
    def __init__(self, a, b, c, x):
        Num.x = x
        Num.a = a
        Num.b = b
        Num.c = c

    def check(self, x):
        if Num.a+Num.b+Num.c == Num.x:
            print('Correct')
        else: print('Incorrect')

print ('Input Num A')
a = int(input())
print ('Input Num B')
b = int(input())
print ('Input Num C')
c = int(input())

print('Input num X')
x = int(input())

f = Num(a, b, c, x)
Num.check(f, x)
