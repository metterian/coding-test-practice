#%%
name = "BBAABB"
# %%
def drop(name):
    i = 0
    if name[-1] != 'A':
        return len(name)-1
    for char in name[::-1]:
        if not char == 'A':
            break
        i += 1
    return len(name[:-i]) -1

# %%

def solution(name)-> int:
    answer = 0
    for char in name:
        answer += min((abs(ord('A') - ord(char))), (abs(ord('Z') - ord(char))+1))

    if name[1] != 'A' and 'A' in name:
        answer += min(drop(name[0]+ "".join(reversed(name[1:]))), drop(name), drop(name[:2] + "".join(reversed(name[2:])))+1)
    elif 'A' in name:
        answer += min(drop(name[0]+ "".join(reversed(name[1:]))), drop(name))

    else:
        answer += (len(name)-1)



    return answer

solution(name)
# %%

# %%
