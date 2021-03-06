#%%

n = 8
x = [-1] * n
answer = 0
visited = [False] * n

# x[i] = row값
# i = col값

def placeQueen(row, col):
    for i in range(col):
        if abs(row-x[i]) == abs(col-i):
            return False

    return True

def nQueens(col):
    global answer
    if col > n-1:
        answer += 1
        return

    for row in range(n):
        # 방문 했으면 다음 행으로 이동
        # 방문 하지 않았으면 행에서 아래 row로 계속 이동
        # 즉 이전에 방문했던 row를 방문 하지 않는 것 -> 같은 row에 놓여 있지 못하게 된다.
        if not visited[row]:
            x[col] = row
            if placeQueen(row, col):
                visited[row] = True
                nQueens(col+1)
                visited[row] = False




nQueens(0)
print(answer)
# %%
