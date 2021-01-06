#%%
n = 'AJKDLSI412K4JSJ9D'
# %%
num_list = []
char_list = []
for i in n:
    if not i.isalpha() :
        num_list.append(i)
    else: char_list.append(i)
num_list = sum(map(int, sorted(num_list)))
print("".join(sorted(char_list))+str(num_list))
# %%
