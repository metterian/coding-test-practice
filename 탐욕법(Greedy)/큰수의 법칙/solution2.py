#%%
n , m, k = list(map(int, '5 7 2'.split()))
A = list (map(int, '3 4 3 4 3'.split()))
# %%
"""


"""
A  = sorted(A)
first, second = A[-1], A[-2]
result = 0

count = m//(k+1)
result += count*first*k
result += count*second

count_rest = int(m%(k+1))
result+= count_rest*first

print(result)
# %%
