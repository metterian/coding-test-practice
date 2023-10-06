"""

스파이가 가진 의상들이 담긴 2차원 배열 clothes가 주어질 때
서로 다른 옷의 조합의 수를 return 하도록 solution 함수를 작성해주세요.


스파이는 하루에 최소 한 개의 의상은 입습니다.
"""
#%%
clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
answer = 5

from collections import Counter, defaultdict
from itertools import chain, combinations


def solution(clothes):
    box = defaultdict(list)
    temp = defaultdict(list)

    for wear, kind in clothes:
        box[wear].append(kind)
        temp[kind].append(wear)

    answer = 0

    # print(list(combinations(list(box.items()), 2)))
    candidate = []
    for i in range(len(temp)):
        candidate.extend(combinations(box.keys(), i + 1))

    for candi in candidate:
        kind = [box[c] for c in candi]
        combi = list(chain(*kind))
        if len(combi) == len(set(combi)):
            answer += 1

    return answer


solution(clothes=clothes)

# %%
