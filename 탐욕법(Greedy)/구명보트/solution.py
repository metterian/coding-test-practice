#%%

people = [70, 80, 50]
limit = 100
boat = []

#%%

def solution(people, limit):
    answer = 0
    people.sort()

    f_cnt =0
    e_cnt =len(people)-1
    while e_cnt - f_cnt >=1:
        if people[f_cnt] +people[e_cnt] <= limit:
            f_cnt +=1
            e_cnt -=1
        else:
            e_cnt -=1
        answer +=1
    if e_cnt == f_cnt:
        answer +=1
    return answer

solution(people, limit)

# %%
