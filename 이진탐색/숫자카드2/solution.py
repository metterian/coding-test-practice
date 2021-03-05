#%%
import sys
input = sys.stdin.readline


from collections import Counter


N = list(map(int, '6 3 2 10 10 10 -10 -10 7 3'.split()))
size_M = 8
M = list(map(int, '10 9 -5 2 3 4 5 -10'.split()))



counter = Counter(N)
N = list(counter.most_common())
n = len(N)
N.sort(key=lambda x:x[0])
#%%
def binary_search(arr, target, left, right):
    while left <= right:
        mid = left + (right-left)//2
        mid_value, count = arr[mid]
        if target == mid_value:
            return count
        elif target < mid_value:
            right = mid -1
        else:
            left = mid + 1

    return 0

#%%


# %%
for m in M:
    print(binary_search(N, m, 0, n-1), end = ' ')

# %%
