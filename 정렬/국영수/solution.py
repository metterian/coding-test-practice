#%%
n = int(input())
students = []
for _ in range(n):
    students.append(input().split())


# %%
students  = sorted(students, key=lambda x : (-int(x[1]), int(x[2]), -int(x[3]), (x[0])))

for stu in students:
    print(stu[0])

# %%
