#%%

s = """()[]{}"""
# %%
# 닫는 것일 때 스택에서 꺼낸다
def isValid(s):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        if char not in table:
            stack.append(char)
        elif not stack or stack.pop() != table[char]:
            return False

    return not stack

isValid(s)
# %%
