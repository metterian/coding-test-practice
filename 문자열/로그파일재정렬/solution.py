#%%
"""
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
"""
logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
# %%
from typing import *

def reorderLogFiles(logs: List[str]) -> List[str]:
    digits = []
    letters = []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters = sorted(letters, key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits

reorderLogFiles(logs)
# %%
def order(x):
    return x.split()[1:], x.split()[0]


def reorderLogFiles(logs: List[str]) -> List[str]:
    digits = []
    letters = []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    letters = sorted(letters, key=order)

    return letters + digits
reorderLogFiles(logs)
# %%
