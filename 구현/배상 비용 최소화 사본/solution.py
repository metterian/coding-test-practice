#%%
N = 4
works = [4,3,3]

def get_cost(works):
    return sum(map(lambda x : pow(x,2), works))


# %%
cost = 1e9
def solution(n, works):
    while n > 0:
        works = sorted(works)
        if works[-1] <= 0:
            break
        works[-1] -= 1
        n -= 1
    return sum([i**2 for i in works])
# %%
