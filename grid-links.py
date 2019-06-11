#For Tech Challenge

def unite(p, q, links):
    pid = links[p[0]][p[1]]
    for i in range(0, len(links)):
        for j in range(0, len(links[i])):
            if links[i][j] == pid:
                links[i][j] = links[q[0]][q[1]]
    return links

inputString = input()
cities = []
row = []
city = ''
for value in inputString:
    if value == '#':
        row.append(int(city))
        cities.append(row)
        row = []
        city = ''
    else:
        if value == '@':
            row.append(int(city))
            city = ''
        else:
            city = city + value
if city != '':
    row.append(int(city))
    cities.append(row)

print(cities)

def least_cost_path(blocks):
    for i in range(len(blocks)):
        for j in range(len(blocks[i])):
            cost = blocks[i][j]
            costs = []
            if i == 0 and j == 0:
                costs.append(cost)
            if i > 0:
                costs.append(cost + blocks[i-1][j])
                if j > 0:
                    costs.append(cost + blocks[i-1][j-1])
                if j < (len(blocks[i]) - 1):
                    costs.append(cost + blocks[i-1][j+1])
            if j > 0:
                costs.append(cost + blocks[i][j-1])
            if j < (len(blocks[i]) - 1):
                costs.append(cost + blocks[i][j+1])
            if i < (len(blocks) - 1):
                costs.append(cost + blocks[i+1][j])
                if j > 0:
                    costs.append(cost + blocks[i+1][j-1])
                if j < (len(blocks[i]) - 1):
                    costs.append(cost + blocks[i+1][j+1])
            blocks[i][j] = min(costs)
    return blocks

print('*********************')
print(least_cost_path(cities))

# links = []
# row = []

# for i in range(0, len(cities)):
#     for j in range(0, len(cities[i])):
#         row.append((i, j))
#     links.append(row)
#     row = []

# red_zone_count = 0
# green_zone_count = 0

# for i in range(len(cities)):
#     for j in range(len(cities[i])):
#         if cities[i][j] == -1:
#             green_zone_count += 1
#             if i > 0 and j > 0 and cities[i-1][j-1] == -1:
#                 links = unite((i-1, j-1), (i, j), links)
#             if i > 0 and cities[i-1][j] == -1:
#                 links = unite((i-1, j), (i, j), links)
#             if i > 0 and j < (len(cities[i]) - 1) and cities[i-1][j+1] == -1:
#                 unite((i-1, j+1), (i, j), links)
#             if j > 0 and cities[i][j-1] == -1:
#                 links = unite((i, j-1), (i, j), links)
#         else:
#             red_zone_count += 1

# print("***links***")
# print(links)
                
