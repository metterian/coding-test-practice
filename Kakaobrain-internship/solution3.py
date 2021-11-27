"""
한 회사가 본사에서 컴퓨터 분석을 하고 있습니다.
컴퓨터들이 한 줄을 따라 간격을 두고 있다.
특정 길이의 인접 시스템 그룹, 즉 각 세그먼트에 대해 컴퓨터에서 사용할 수 있는 최소 디스크 공간을 결정합니다.
이 값들 중 최대값을 답변으로 반환하십시오.


"""
#%%
input = open('input.txt', 'r').readline



# if __name__ == '__main__':
x = int(input().strip())

space_count = int(input().strip())

space = []

for _ in range(space_count):
    space_item = int(input().strip())
    space.append(space_item)

    # result = segment(x, space)

# %%

max_num = 0
for i in range(space_count):
    if i + x <= space_count:
        minimum = space[i:i+x]
        if max_num < min(minimum):
            max_num = min(minimum)
    else:
        break

# %%

count = 0
max_num = 0
for i in range(space_count - x + 1):
    count += 1
    minimum = space[i: i + x]
    if max_num < min(minimum):
        max_num = min(minimum)
max_num
# %%
max_num = 0
sorted_space = sorted(space)
for i in range(space_count - x + 1):
    minimum = sorted_space[i: i + x]
    print(minimum)
    if max_num < min(minimum):
        max_num = min(minimum)

max_num
# %%
[max_num for i in range(space_count - x + 1) if max_num < min(sorted_space[i: i + x])]
# %%
