#%%
s = '1100011011'
# %%
def solution(s, basis):
    block = s.split(str(basis))
    return len(block) - block.count('')

print(solution(s, 0))
print(solution(s,1))
# %%
