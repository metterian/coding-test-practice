#%%
import random
import matplotlib.pyplot as plt

# %%
import random

TRIALS = 10000 # 10만 번의 실험
same_birthdays = 0 # 생일이 같은 실험의 수

# 10만번의 실험 진행
for _ in range(TRIALS):
    birthdays = []
    # 23명이 모몄을때, 생일이 같은 경우 same_birthdays += 1
    for i in range(23):
        birthday = random.randint(1,365)
        if birthday in birthdays:
            same_birthdays += 1
            break
        birthdays.append(birthday)

print(f'{same_birthdays/TRIALS *100}%')
# %%
