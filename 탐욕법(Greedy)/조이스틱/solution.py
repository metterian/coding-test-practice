#%%
name = "JEROEN"
# %%

def reversed_count_move(name) -> int:
    reversed_name = list(reversed(name))
    count = 1

    for char in reversed_name:
        if not char == 'A':
            return count
        else:
            count += 1

    return count

def count_move(name) -> int:
    count = 1
    for char in name[1:]:
        if not char == 'A':
            return count
        else:
            count += 1
    return count




def solution(name)-> int:
    answer = 0
    for char in name:
        answer += min((abs(ord('A') - ord(char))), (abs(ord('Z') - ord(char))+1))



    return answer

solution(name)
# %%
