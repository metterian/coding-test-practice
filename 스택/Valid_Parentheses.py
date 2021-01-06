#%%
s = "()[]{}"
#%%
stack = []
table = {
    ')' :'(',
    '}' : '{',
    ']' : '['
}


# %%

for char in s:
    if char not in table:
        stack.append(char)
    elif not stack or table[char] != stack.pop():
        print(False)
print(len(stack) == 0)

# %%
