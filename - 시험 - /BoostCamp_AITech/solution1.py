#%%
from collections import Counter
s = "abebeaedeac"
Counter(s)

answer = 0
for char in Counter(s):
    if Counter(s)[char]%2 != 0:
        answer+=1
print(answer)
# %%

# %%
