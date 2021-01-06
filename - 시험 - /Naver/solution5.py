#%%
ballons = [[2, 2], [4, 4], [1, 4], [-1, -4]]
# %%

def solution(ballons):
    det = []
    for x,y in ballons:
        if x <0 and y <0:
            det.append(round(- x/y, 3))
        else:
            det.append(x/y)
    print(det)
    return len(set(det))
solution(ballons)
# %%
