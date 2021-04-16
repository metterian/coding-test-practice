#%%






# %%
math_scores = [70, 65, 90, 80, 50]
english_scores = [40, 20, 30, 60, 50]
def solution(math_scores, english_scores):
    n = len(english_scores)

    math_scores = [[i, score] for i, score in enumerate(math_scores)]
    english_scores = [[i, score] for i, score in enumerate(english_scores)]

    math_scores = sorted(math_scores, key=lambda x: x[1], reverse=True)
    english_scores = sorted(english_scores, key=lambda x: x[1], reverse=True)

    for i in range(n):
        math_scores[i].append(i+1)
    math_scores.sort(key=lambda x:x[0])

    for i in range(n):
        english_scores[i].append(i+1)
    english_scores.sort(key=lambda x:x[0])

    answer  = 0
    for i in range(n):
        for j in range(i+1,n ):
            if (math_scores[i][2] < math_scores[j][2] and english_scores[i][2] < english_scores[j][2]) or ( math_scores[i][2] > math_scores[j][2] and english_scores[i][2] > english_scores[j][2]):
                answer += 1

    return (answer)
solution(math_scores, english_scores)
# %%
