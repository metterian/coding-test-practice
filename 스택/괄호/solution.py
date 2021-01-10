# %%
def Valid_PS(bracket):
    stack = []
    for char in bracket:
        if char == '(':
            stack.append(char)
        elif not stack or stack.pop() != '(':
            return False
    return not stack

#%%
t = int(input())
brackets = []
for _ in range(t):
    if Valid_PS(input()):
        print("YES")
    else:
        print("NO")
