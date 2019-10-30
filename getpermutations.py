a = ['1', '2', '3', '5', '6']

def getpermutations(a, k):
    if (k == 0):
        return [""]
    perms = []
    for i in range(len(a)):
        a_n = a[:i] + a[i+1:]
        for x in getpermutations(a_n, k-1):
            perms.append(x + a[i])
    return perms

print("hellow world")
for x in a:
    print(x)
print(getpermutations(a, 2))    