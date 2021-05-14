#%%
number = 7

def compare(number, next):
    digit = 0
    print(number)
    for i, j in zip(number, next):
        if i != j:
            digit += 1

    return digit
#%%
def solution(numbers):
    answer = []
    for number in numbers:
        next = number + 1
        while True:
            digit = compare(format(number, 'b').zfill(16), format(next, 'b').zfill(16))
            if digit <= 2:
                break
            next += 1
        answer.append(next)
    return answer
solution([2,7])
# %%
