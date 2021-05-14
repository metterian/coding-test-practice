#%%
s = '0111111010'

min_val = '1'*1000000
def get_sorted(digit):
    global min_val

    numbers = []
    if '110' not in digit:
        return

    left, right = digit.split('110', 1)

    for i in range(len(left)+1):
        number = left[:i]+'110'+left[i:]+right
        tail = get_sorted(number[i+3:])
        if tail:
            number = number[:i+3]+tail
        numbers.append(number)
    for i in range(len(right)+1):
        number = left + right[:i]+'110'+right[i:]
        numbers.append(number)
    val = min(numbers)
    return val

get_sorted(s)
#%%
def solution(s):
    for
# %%
