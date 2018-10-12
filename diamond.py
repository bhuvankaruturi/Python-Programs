def recursive(name):
    print(name)

x = 0
y = 10
while (x<10):
    recursive('~' * y + '*' * (2 * x + 1) + '~' * y)
    x += 1
    y -= 1
    
while (x>=0):
    recursive('~' * y + '*' * (2 * x + 1) + '~' * y)
    x -= 1
    y += 1