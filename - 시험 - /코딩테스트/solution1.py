#%%
from functools import reduce
n =3462
n = str(n)

def multiply(arr):
    return reduce(lambda x, y: x * y, arr)
#%%
def solution(num):
    while(True):
        n = str(num)
        front, end  = n[:len(n)//2], n[len(n)//2:]
        front, end = list(map(int, front)), list(map(int, end))
        if multiply(front) == multiply(end) and len(n)%2==0:
            break
        else:
            num+=1
    return num


solution(3462)
# %%
