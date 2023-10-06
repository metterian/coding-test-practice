# %%
s = "[](){}"


# %%


def is_valid(s):
    stack = []
    # bracket = {"[": "]", "{": "}", "(": ")"}
    bracket = {"]": "[", "}": "{", ")": "("}

    for char in s:
        if not stack or char not in bracket:
            stack.append(char)
        elif stack[-1] == bracket[char]:
            stack.pop()

    return not stack


# %%
def solution(s):
    answer = 0
    for i in range(len(s)):
        answer += is_valid(s[i:] + s[:i])
    return answer


# %%
