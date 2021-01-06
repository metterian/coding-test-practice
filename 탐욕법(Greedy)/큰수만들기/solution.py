#%%
number = "1231234"
k = 3

# %%
import sys
import numpy as np

def solution(number, k):
    number = list(number)
    answer = []
    digit = len(number) -k
    start, end = np.argmax(number[0:-digit+1]) , digit
    answer.append(number[start])
    while digit -1 > 0:
        digit -= 1
        if digit  == 1:
            answer.append(number[-1])
            break
        max_index = np.argmax(number[start+1:-digit+1])
        start += max_index+1
        answer.append(number[start])
        end = digit
    return "".join(answer)









print(solution(number, k))
# %%

# %%
