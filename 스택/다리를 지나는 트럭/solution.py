# %%
bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

# %%


def solution(bridge_length, weight, truck_weights):
    sec = 0
    queue = [0]*bridge_length


    while queue:
        queue.pop(0)
        if truck_weights and (sum(queue) + truck_weights[0]) <= weight:
            queue.append(truck_weights.pop(0))
        elif truck_weights:
            queue.append(0)

        sec +=1

    return sec
solution(bridge_length, weight, truck_weights)

# %%

# %%
