#%%
n = 9
A = list(map(int, '5 12 7 10 9 1 2 3 11'.split()))
X = 13
A.sort()



answer = 0
left, right = 0, n -1
while left < right:
    if A[left] + A[right] == X:
        answer += 1
        left += 1
        right -= 1

    elif A[left] + A[right] > X:
        right -= 1

    else:
        left += 1

print(answer)
# %%
