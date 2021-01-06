#%%
T = [73, 74, 75, 71, 69, 72, 76, 73]
stack = []

days = []
for i, t in enumerate(T):
    wait = 0
    stack.append(t)
    while i< len(T)-1:
        if stack[-1] < T[i+1]:
            wait+=1
            break
        else:
            wait +=1
            i+=1
    stack.pop()
    days.append(wait)

# %%
