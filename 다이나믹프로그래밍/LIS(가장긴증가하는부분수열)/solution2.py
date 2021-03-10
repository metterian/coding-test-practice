#%%

A =list((map(int, ('0 '+input()).split())))
n = 6
# %%
from collections import defaultdict

def solution(n):
    D = defaultdict(lambda :0)

    for i in range(1, n+1):
        for j in range(i):
            if A[i] > A[j]:
                D[i] = max(D[j]+1, D[i])


    return max(D.values())

solution(n)

# %%
