

#%%
n = input()
A, B = list(map(int,(n.split())))
# A, B = 2 , 12

# %%
c_num =0
for i in range(A, B+1):
    c_num +=bin(i).count('1')

print(c_num)
# %%
