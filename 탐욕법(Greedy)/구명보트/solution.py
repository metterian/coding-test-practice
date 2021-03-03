#%%

people = [70, 50, 80, 50]
limit = 100


#%%


def solution(people, limit):

    people.sort(reverse=True)
    boat = []

    cnt = 0

    left, right = 0, len(people)-1

    while left < right:
        two_sum = people[left] + people[right]
        if two_sum == limit:
            boat.append([people.pop(left), people.pop(right)])
        elif two_sum > limit :
            left += 1
        else:
            right -= 1

    print(boat)




    # print(boat)


    return boat

solution(people, limit)

# %%
