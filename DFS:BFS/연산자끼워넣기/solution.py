#%%
n = 6
A = [1,2,3,4,5,6]
add ,sub ,mul, div = [2,1,1,1]
# %%



# %%
import math

min_value = (math.inf)
max_value = -(math.inf)


def solution(i, now):
    global min_value, max_value,add ,sub ,mul, div

    if i == n:
        if now > max_value:
            max_value = now
        if now < min_value:
            min_value = now
    else:
        if add:
            add -= 1
            solution(i+1, now+A[i])
            add+=1
        if sub:
            sub -= 1
            solution(i+1, now-A[i])
            sub += 1
        if div:
            div -= 1
            solution(i+1, int(now/A[i]))
            div +=1
        if mul:
            mul -= 1
            solution(i+1, now*A[i])
            mul +=1

solution(1, A[0])
print(max_value, min_value)







# %%
