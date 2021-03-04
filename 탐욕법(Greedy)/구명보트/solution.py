#%%

people = [70, 80, 50]
limit = 100
boat = []

#%%

def solution(people, limit):
    answer  = 0
    people.sort()
    left, right = 0, len(people) - 1

    while left < right:
        if people[left] + people[right] <= limit:
            right -= 1
            left += 1
        else:
            right -= 1
        answer += 1


    if left == right:
        answer +=1
    return answer

solution(people, limit)

# %%
