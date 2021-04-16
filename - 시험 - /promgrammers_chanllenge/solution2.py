#%%
s = "[](){}"

# %%
def isValid(bracket):
    stack = []
    table = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in bracket:
        if char not in table:
            stack.append(char)
        elif not stack or stack.pop() != table[char]:
            return False

    return not stack

#%%
def solution(s):
    answer = 0
    for x in range(len(s)):
        bracket = s[x:] + s[:x]
        if isValid(bracket):
            answer += 1

    return answer


solution("}]()[{")
# %%
