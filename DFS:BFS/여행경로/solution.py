#%%
# BEGIN: yz1x2c3v4b5n
from collections import defaultdict, deque

tickets = [["ICN", "B"], ["B", "C"], ["C", "ICN"], ["ICN", "D"], ["ICN", "E"], ["E", "F"]]
# tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]



course = defaultdict(list)
for start, end in tickets:
    course[start].append(end)
course = {k: sorted(v, reverse=True) for k, v in course.items()}

print(course)

route = []


queue = deque()
queue.append("ICN")

while queue:
    print(f"queue: {queue}")
    visit = queue[-1]

    if visit not in course or len(course[visit]) == 0:
        route.append(queue.pop())
    else:
        queue.append(course[visit].pop())


print(route[::-1])

# END: yz1x2c3v4b5n
# %%
