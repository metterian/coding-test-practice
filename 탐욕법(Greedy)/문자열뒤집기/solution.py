#%%
S = '0001100100'
s = S[:]
# %%

count0 = 0
count1 = 1


if S[0] == '1':
    count0 +=1
else:
    count1 +=1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        if S[i+1] == '1':
            count1+=1
        elif S[i+1] == '0':
            count0 +=1

print(count0, count1)




# %%

# %%
