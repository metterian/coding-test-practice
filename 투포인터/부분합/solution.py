#%%
n, s = 10, 15
A = list(map(int, '5 1 3 5 10 7 4 9 2 8'.split()))

# %%
prefixSum = A[:]
for i in range(1, len(A)):
    prefixSum[i] += prefixSum[i-1]