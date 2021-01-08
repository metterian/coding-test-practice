#%%
s = '0001100'
# %%
def solution(s, basis):
    block = s.split(str(basis))
    return len(block) - block.count('')
print(min(solution(s, 0),solution(s,1)))
# %%
