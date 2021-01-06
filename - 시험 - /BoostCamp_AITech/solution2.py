#%%

arr = [1, 1, 3, 3, 2, 2, 4, 5, 1, 1, 1, 3, 3, 3]
answer = 0
def find_pack(arr):
    arr.append(1e-9)
    global l, answer
    if sum(arr[:-1])  == 1:
        return
    answer+=1
    pack =[]
    same = 1
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            same+=1
        else:
            pack.append(same)
            same = 1
    find_pack(pack)
def solution(arr):
    find_pack(arr)
    return answer

print(solution(arr))

# %%
