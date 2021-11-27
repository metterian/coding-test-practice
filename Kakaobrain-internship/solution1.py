#%%
import os
input = open('input1.txt', 'r').readline


"""
비상 부분 문자열은 각 문자의 매핑된 값의 합이 그 길이로 나누어지는 문자열이다.

문자열 "입력"이 주어지면 비어 있지 않은 비상 부분 문자열의 총 수를 계산합니다.
"""


keymap = {
    "a": 1,
    "b": 1,
    "c": 2,
    "d": 2,
    "e": 2,
    "f": 3,
    "g": 3,
    "h": 3,
    "i": 4,
    "j": 4,
    "k": 4,
    "l": 5,
    "m": 5,
    "n": 5,
    "o": 6,
    "p": 6,
    "q": 6,
    "r": 7,
    "s": 7,
    "t": 7,
    "u": 8,
    "v": 8,
    "w": 8,
    "x": 9,
    "y": 9,
    "z": 9
}
#%%
def is_divisible(string):
    if len(string) == 1:
        return 1
    mapped = [keymap[s] for s in string]
    if sum(mapped) % len(mapped):
        return 0
    else:
        return 1


def countSubstrings(input_str):
    answer = 0
    l = len(input_str)
    for window in range(1, l+1):
        for i in range(l):
            string = input_str[i:i+window]
            if window == len(string):
                answer += is_divisible(string)
            else:
                break
    return answer


if __name__ == '__main__':
    input_str = input().strip()
    print(input_str)

    # input_str = 'asdf'

    result = countSubstrings(input_str)

    print(result)

# %%
input_str = 'asdf'


answer = 0
l = len(input_str)
for k in range(1,l+1):
    for i in range(l - k + 1):
        string = (input_str[i: i + k])
        answer += is_divisible(string)

print(answer)

# %%
