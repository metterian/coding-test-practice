#%%
pickup = [0,4,5]
drop =   [3,5,7]
tip =    [1,2,2]
# %%
data = [[p, d, t, (d-p+t)] for p,d,t in zip(pickup, drop, tip)]
data = sorted(data, key=lambda x: ((x[1] - x[0] + x[2]), x[1], x[0]), reverse=True)
print(data)

#%%


def taxiDriver(pickup, drop, tip):
    answer =[]
    starts = []
    starts.append(data[0][0])


    flag = 0
    end = data[0][1]
    answer.append(data[0])
    for i in range(1, len(data)):
        for j in answer:
            if data[i][0] in range(j[0]+1,j[1]) or data[i][1] in range(j[0]+1, j[1]):
                flag = 1
        if flag:
            flag = 0
            continue
        answer.append(data[i])


    n = 0
    for i in answer:
        n+= i[3]

    print(answer)
    return(n)
taxiDriver(pickup, drop, tip)



# %%

# %%
