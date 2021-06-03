#%%



# %%
name  = 'JAN'


def solution(name):
    num = 0
    lmov = 0
    for N in name:
        diff = min((ord(N) - ord('A')), (ord('Z') - ord(N)+1))
        if not diff:
            continue
        else:
            lmov += 1
        num += diff

    rmov = len(name) -1




    return min(rmov, lmov) + num


solution('JEROEN')
# %%
