#%%
n = int(input())
students = list(map(int, input().split()))
b,c = map(int, input().split())
# %%
B = list(map(lambda x : 1 if x > 0 else 0, students))
students = list(map(lambda x : 0 if x - b < 0 else  x-b, students))
C = list(map(lambda x : x//c if x % c == 0 else x // c + 1, students))

print(sum(B)+sum(C))
# %%
