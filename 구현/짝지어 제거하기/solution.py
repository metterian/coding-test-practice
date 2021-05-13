#%%
s= 'baab'



def solution(s):
    chars = list(set(s))*3
    for char in chars:
        if '' not in s.split(char*2):
            continue
        s = "".join(s.split(char*2))
    return int(len(s) == 0)
solution(s)
# %%

# %%
