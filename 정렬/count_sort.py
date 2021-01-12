#%%

# - 계수 정렬은 동일한 값을 가지는 데이터가 여러개 등장 할 때 효과적으로 사용 가능
array = [7,5,9,0,3,1,6,2,9,1,4,8,0,5,2,]
# %%
def CountSort(array):
    # 모든 범위를 포함하는 리스트 선언(모든 값을 0으로 초기화)
    count = [0] * (max(array)+1)

    for i in range(len(array)):
        count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

    for i in range(len(count)):
        for j in range(count[i]):
            print(i, end=' ') # 등장한 횟수 만큼 인덱스 출력

CountSort(array)
# %%
