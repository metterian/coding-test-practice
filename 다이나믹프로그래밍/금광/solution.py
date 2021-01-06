#%%
import numpy as np
T = 2
A = [1,3,3,2,2,1,4,1,0,6,4,7]
B = [1,3,1,5,2,2,4,1,5,0,2,3,0,6,1,2]
A = np.reshape(A, (3,4))
B = np.reshape(B, (4,4))

# %%
def solution(array):
    row, col = array.shape
    row, col = row-1, col-1
    dp = [ [0] * (col+1) for _ in range(row+1)]

    for r in range(row +1):
        dp[r][0] = array[r][0]


    for c in range(1, col+1):
        for r in range(row+1):
            # 왼쪽 위
            if 0 <= r -1 and 0<= c - 1 <= col:
                left_up = dp[r-1][c-1]
            else:
                left_up = 0

            # 왼쪽
            if 0<= c-1 <= col:
                left = dp[r][c-1]
            else:
                left = 0

            #왼쪽 아래
            if r+1 <= row and 0<= c-1 <=col:
                left_down = dp[r+1][c-1]
            else:
                left_down = 0

            dp[r][c] = array[r][c] + max(left_up, left, left_down)

    return dp

np.array(solution(A))[:, -1].max()
# %%
