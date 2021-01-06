#%%
from itertools import combinations
from itertools import product
from collections import Counter

arr1 = ["()", "(()", "(", "(())"]
arr2 = [")()","()", "(())", ")()"]
items = [arr1, arr2]
items = [f+e for f,e in product(arr1, arr2)]

#%%


def check(bracket):
    stack = []
    for i, letter in enumerate(bracket):
        if letter == '(': stack.append(i)
        elif letter == ')':
            if stack:
                stack.pop()
            else:
                stack.append(i)
                return len(stack)==0
    return len(stack)==0

Counter(list(map(check, items)))[True]
# %%
