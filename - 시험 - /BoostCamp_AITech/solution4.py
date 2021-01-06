#%%
n = 9
arr = [1 for _ in range(n)]
a,b,c = 2,0,1
for i in range(n):
    if i!=0 and i%4==0:
        b = a*(a+1)*(a+2)
        arr[i] = b
        a+=1
        b = 0
    else:
        arr[i] = c*(c+1)
        c+=1
print(arr[n-1])
# %%
