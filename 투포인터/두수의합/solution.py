#%% 
n = 9
A = list(map(int, '5 12 7 19 9 1 2 3 11'.split()))
x = 13
# %%
A.sort()
answer = 0
start, end = 0, n-1

while start != end:
    twoSum = A[start] + A[end]
    if twoSum == x:
        answer+=1
        start +=1

    elif twoSum < x:
        start += 1
    else:
        end -= 1

    


print(answer)
# %%
