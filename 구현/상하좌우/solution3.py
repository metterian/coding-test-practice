N = int(input())
plans = list(map(str, input().split()))

x, y = 0, 0
move_types = ["L", "R", "U", "D"]
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


location = []

for row in range(N):
    loc = []
    for col in range(N):
        loc.append([row+1, col+1])
    location.append(loc)

print(location)

for plan in plans:
    for i, move_type in enumerate(move_types):
        if plan == move_type:
            nx = x + dx[i]
            ny = y + dy[i]
    if ny < 0 or nx < 0 or nx > N-1 or ny > N-1:
        continue
    x = nx
    y = ny
print(x, y)

print(location[x][y])


