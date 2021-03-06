#%%

n = 8
x = [-1] * n
answer = 0
visited = [False] * n

# x[i] = row값
# i = col값

def placeQueen(row, col):
    for i in range(col):
        if x[i] < 0 or abs(row-x[i]) == abs(col-i) or x[i] == row:
            return False

    return True

def nQueens(col):
    global answer
    if col > n-1:
        answer += 1
        return

    for row in range(n):
        # 방문 했으면 다음 행으로 이동
        if visited[row]:
            continue
        # 방문 하지 않았으면 행에서 아래 row로 계속 이동
        x[col] = row
        if placeQueen(row, col):
            visited[row] = True
            nQueens(col+1)
            visited[row] = False




nQueens(0)
print(answer)
# %%
