# Q20

print("======= a =======")
for x in range(1,200):
    if x % 4 == 0:
        print('{0:.2f}'.format(x))

print("======= b =======")
#while x < 200:
#    if (x % 4 == 0):
#        x = x + 1
#        print('{0:d}'.format(x))
#        x = x + 2

print("======= c =======")
for x in range(1,200):
    if x % 2 == 0:
        print('{0:d}'.format(x))

print("======= d =======")
for x in range(1,200):
    if x % 4 == 0:
        print('{0:d}'.format(x))

print("======= e =======")
for x in range(1,200):
    if x % 4 != 0:
        print('{0:d}'.format(x))
    x = x + 1
