#%%
from collections import Counter
s = "bbaabaaaab"
k = 8


def leastSting(k, s):
    n = len(s)
    sp = [ s[i:i+k] for i in list(range(n))[::k]]
    sp.append('')
    string = []
    coff = 1
    print(sp)
    for i in range(len(sp)-1):
        if sp[i] == sp[i+1]:
            coff +=1
        if coff<=1 and sp[i] != sp[i+1]:
            string.append(sp[i])
        elif sp[i] != sp[i+1]:
            string.append(str(coff)+sp[i])
            coff = 1

    print("".join(string))
    return len("".join(string))

# %%
lenths = [ leastSting(k, s) for k in range(1,len(s)+1)]
lenths
# %%
"""

bbaabaaaab
zzzbbabbabba

"""
