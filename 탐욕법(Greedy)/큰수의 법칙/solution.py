#%%
n , m, k = list(map(int, '5 8 3'.split()))
A = list (map(int, '2 4 5 4 6'.split()))
# %%
A = sorted(A)

answer = 0
t, t2= 0, 0
oper_t = 0
i = 1
while(oper_t< m):
    if t < k:
        answer += A[-i]
        t+=1
    else:
        answer += A[-(i+1)]
        if A[-(i+1)] < A[-i]:
            t = 0
        elif t2 < k:
            t2+=1
        else:
            t=0


    oper_t += 1


print(answer)

# %%
