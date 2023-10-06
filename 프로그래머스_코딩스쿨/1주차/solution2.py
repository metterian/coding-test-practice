#%%

from collections import Counter

# bell = [1, 2, 1, 1, 1, 2, 2, 1]
bell = [2, 2, 1, 1, 2, 2, 2, 2, 2, 2, 1]


def solution(bell):
    answer = 0
    bell = list(map(str, bell))
    color_map = {"1": "red", "2": "green"}
    bell = [color_map[b] for b in bell]

    counter = Counter(bell)

    max_color = min(counter)
    max_color_cnt = counter[max_color]

    max_len = min(counter[max_color] * 2, len(bell))
    print(max_len)

    for l in range(max_len, 0, -1):  # 최대 길이 6부터 점점 1씩 감소
        # 길이가 6인 최대 길이로 만들 수 있는 index 구간
        print(f"LENGTH: {l}")
        for start in range(len(bell) - l + 1):
            end = start + l
            max_color_cnt = l // 2
            print(Counter(bell[start:end]))
            candi = [True if v == max_color_cnt else False for _, v in Counter(bell[start:end]).items()]
            print(candi)
            if all(candi):
                answer = l
                return answer
        print("\n")
    return answer


solution(bell=bell)
# %%
