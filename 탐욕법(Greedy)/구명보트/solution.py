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
        if people[left] + people[right] == limit:
            people.pop(right)
            boat.append([people[left], people[right]])
            right = len(people) - 1
            left += 1

        elif people[left] + people[right] > limit:
            if left + 1 == right:
                boat.append([people[left], people.pop(right+1)])
                right = len(people) -1

            else:
                right -= 1

        else:
            if left + 1 == right:
                boat.append([left, people(right)])
                left += 1
                right = len(people)
            else:
                right -=1



    # print(boat)


    return boat

solution(people, limit)

# %%
