#%%
expression ="100-200*300-500+20"
from itertools import permutations


def calculate(priority, i, expression):
    if i == 2:
        return str(eval(expression))

    if priority[i] == '*':
        result = eval("*".join([calculate(priority, i+1, e) for e in expression.split('*')]))
    if priority[i] == '+':
        result = eval("+".join([calculate(priority, i+1, e) for e in expression.split('+')]))
    if priority[i] == '-':
        result = eval("-".join([calculate(priority, i+1, e) for e in expression.split('-')]))

    return str(result)

import sys
def solution(expression):
    answer = 0
    priorities = list(permutations(['*', '-', '+'] ,3))
    for priority in priorities:
        result = calculate(priority, 0, expression)
        answer = max(answer, abs(int(result)))

    return answer

solution(expression)
# %%
