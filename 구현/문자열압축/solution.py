
#%%
def compressed(s, step):
    n = len(s)
    compress = [s[start:start+step] for start in range(0, n, step)]
    string = []

    compress.append('')
    coef = 0
    for i in range(len(compress)-1):
        if compress[i] == compress[i+1]:
            coef += 1

        elif coef:
            string.append(str(coef+1)+compress[i])
            coef = 0

        else:
            string.append(compress[i])
    string = "".join(string)
    return len(string)

#%%
def solution(s):
    n = len(s)
    answer = n
    for step in range(1, n-1):
        answer = min(answer, compressed(s,step))
    return answer
print(solution('aabbaccc'))
