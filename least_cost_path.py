#Path with the least cost

inputString = input()
blocks = []
row = []
cost = ''
for value in inputString:
    if value == '#':
        row.append(int(cost))
        blocks.append(row)
        row = []
        cost = ''
    else:
        if value == '@':
            row.append(int(cost))
            cost = ''
        else:
            cost = cost + value
if cost != '':
    row.append(int(cost))
    blocks.append(row)

print(blocks)

def least_cost_path(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            cost = blocks[i][j]
            if i == 0 and j == 0:
                minCost = cost
            if i > 0 and j > 0:
                currCost = cost + blocks[i-1][j-1]
                minCost = currCost
            if i > 0:
                currCost = cost + blocks[i-1][j]
                if currCost < minCost:
                    minCost = currCost
            if i > 0 and j < (len(blocks[i]) - 1):
                currCost = cost + blocks[i][j+1]
                if currCost < minCost:
                    minCost = currCost
            if j > 0:
                currCost = cost + blocks[i][j-1]
                if currCost < minCost:
                    minCost = currCost
            blocks[i][j] = minCost
    return blocks

print("**********************")
print(least_cost_path(blocks))