#%%
def knapSack(W, s, p, n):

    # Base Case
    if n == 0 or W == 0:
        return 0


    if s[n - 1] > W:
        return knapSack(W, s, p, n - 1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(
            p[n - 1] + knapSack(W - s[n - 1], s, p, n - 1),
            knapSack(W, s, p, n - 1),
        )


# end of function knapSack

# To test above function
p = [60, 100, 120]
s = [10, 20, 30]
W = 50
n = len(p)
print(knapSack(W, s, p, n))

# %%
