#%%

from collections import Counter


input = open('input.txt', 'r').readline 


# %%
n = int(input())
cases = [input().split() for _ in range(n)]

# %%
def annagram(pair):
    a, b = pair
    if len(a) != len(b):
        return False
        
    a_counter = Counter(a)
    b_counter = Counter(b)

    for k, v in a_counter.items():
        if k in b_counter:
            return v == b_counter[k]
        else:
            return False
# %%
if __name__ == "__main__":
    for case in cases:
        a, b = case
        flag  = '' if annagram(case) else " NOT"
        print(f"{a} & {b} are{flag} anagrams.")
# %%
