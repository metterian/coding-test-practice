#%%


paper = [7, 3, -7, 5, -3]


# %%
def fold(paper, pivot):
    if len(paper) <= 1:
        return paper
    if len(paper) == 2:
        return sum(paper)


    right = paper[pivot+1:]
    left = list(reversed(paper[:pivot+1]))

    for i in range(min(len(left), len(right))):
        if len(right) > len(left):
            right[i] += left[i]
        else:
            left[i] += right[i]
    if len(right) > len(left):
        return right
    else:
        return left
# %%

answer = max(paper)
n = 2
def recursion(paper):
    global answer,n

    if n <= 0:
        return

    for pivot in range(len(paper)-1):
        answer = max(answer, max(fold(paper, pivot)))

    n -= 1
    for pivot in range(len(paper)-1):
        recursion(fold(paper, pivot))


recursion(paper)
print(answer)
# %%

# %%
