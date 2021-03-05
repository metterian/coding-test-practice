#%%
import sys
input = sys.stdin.readline
from collections import Counter


N = list(map(int, '6 3 2 10 10 10 -10 -10 7 3'.split()))
size_M = 8
M = list(map(int, '10 9 -5 2 3 4 5 -10'.split()))



counter = Counter(N)
for target in M:
    if target in counter:
        print(counter[target], end=' ')
    else:
        print(0, end= ' ')
