t = int(input())

while t > 0:
    t = t-1;
    (n, m) = tuple(map(int, input().split()))
    pathsList = []
    for i in range(n):
        tempList = []
        for j in range(m):
            if i == 0 or j == 0:
                tempList.append(1)
            else:
                tempList.append(pathsList[i-1][j] + tempList[j-1])
        pathsList.append(tempList)
    print(pathsList[n-1][m-1] % (10**9 + 7))