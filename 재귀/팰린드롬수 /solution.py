#%%
"""

121 -> yes
1231 -> no
12421 -> yes
0


"""
# %%


numbers = []
flag = True
while flag:
    number = int(input())
    if number:
        numbers.append(str(number))
    else:
        flag = False


#%%
def is_check(number: str, start: int, end: int) -> bool:
    if len(number) == 1:
        return "yes"
    if number[start] == number[end] and start < end:
        if start + 1 >= end - 1:
            return "yes"
        return is_check(number, start + 1, end - 1)
    else:
        return "no"


for number in numbers:
    start = 0
    end = len(number) - 1

    print(is_check(number, start, end))


# %%
