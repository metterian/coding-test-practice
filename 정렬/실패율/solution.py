#%%



def loss(i, stages):
    not_clear = len([x for x in stages if x == i])
    trial = len([x for x in stages if x >= i ])
    
    return not_clear/trial

#%%
def solution(N, stages):

    count = []
    for i in range(1, N+1):
        count.append([i, loss(i, stages)])
    
    
    answer = sorted(count, key = lambda x: x[1], reverse=True)

    return [x for x, loss in answer]

solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
# %%
