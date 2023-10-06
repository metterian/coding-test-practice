#%%
answer = 0
def solution(numbers, target = 0):
    global answer

    if sum(numbers) == target:
        answer +=1
        print(numbers)
        return
    elif not numbers:
        return
    solution(numbers[1:], target - numbers[0])
    numbers[0] *= -1
    solution(numbers[1:], target - numbers[0])

    return answer

solution([8,3,5,7,3,4])
    # %%
