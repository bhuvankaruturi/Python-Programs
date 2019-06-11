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
            costs = []
            if i == 0 and j == 0:
                costs.append(cost)
            if i > 0 and j > 0:
                costs.append(cost + blocks[i-1][j-1])
            if i > 0:
                costs.append(cost + blocks[i-1][j])
            if i > 0 and j < (len(blocks[i]) - 1):
                costs.append(cost + blocks[i-1][j+1])
            if j > 0:
                costs.append(cost + blocks[i][j-1])
            blocks[i][j] = min(costs)
    return blocks

print("**********************")
print(least_cost_path(blocks))