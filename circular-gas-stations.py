'''
    lis[][0]:Petrol
    lis[][1]:Distance
'''
def tour(lis, n):
    #Code here
    start_point = -1
    dist_diff = 0
    deficit = 0
    for i in range(n):
        dist_diff += lis[i][0] - lis[i][1]
        if dist_diff >= 0: #continue moving forward as long as the deficit petrol is positive
            if start_point == -1:
                start_point = i
        if dist_diff < 0: #reset start point to -1
            start_point = -1
            deficit += dist_diff
            dist_diff = 0
        print("%d, %d, %d"%(dist_diff, deficit, start_point))
    if deficit + dist_diff >= 0:
        return start_point
    else:
        return -1

t = int(input())
for i in range(t):
    n = int(input())
    arr=list(map(int, input().strip().split()))
    lis=[]
    for i in range(1, 2*n, 2):
        lis.append([ arr[i-1], arr[i] ])
    #print n, arr
    print(tour(lis, n))
