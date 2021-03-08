#%%
def groupCheck(chars, alphabet):
    base = alphabet

    for char in chars:
        if char != alphabet:
            base = char
        if char != base:
            return False
    return True

alphabets = list()
n  = int(input())
for _ in range(n):
    flag = True
    chars = input()
    for alphabet in set(chars):
        if  groupCheck(chars, alphabet):
            alphabets.append(alphabet)


print(len(set(alphabets)))


# %%
