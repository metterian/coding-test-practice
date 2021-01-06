#%%
s = 'cbacdcbc'
s = list(set(s))
stack = []
least_char = min(s)
stack.append(least_char)
i = 0
while stack:
    if s[i] > least_char:
        stack.append(s[i])
    elif s[i] == least_char:
        print(s[i], end='')
    else:
        p =stack.pop()
        print(p)
        if p < s[i]:
            print(p, end='')
        else:
            stack.append(p)
    i+=1




# %%
