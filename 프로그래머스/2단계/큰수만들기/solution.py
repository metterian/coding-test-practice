#%%
import math
def find_max(numbers):
    max_num = - math.inf
    for number in numbers:
        if number == '9':
            return '9'
        max_num = max(max_num, int(number))
    return str(max_num)

def solution(number, k):
    n = len(number)
    answer = ''


    l = n - k
    m = l
    for _ in range(m):
        n = len(number)
        if n <= l:
            answer += number
            break

        num = find_max(number[:n-l+1])
        answer += num
        number = number[number.index(num)+1:]
        l -= 1

    return answer





solution('1924', 2)
# %%
