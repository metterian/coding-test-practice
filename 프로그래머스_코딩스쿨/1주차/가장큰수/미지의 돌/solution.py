




floor = 2554
answer = 1e+6
chance = 0
floor = 1e+6

def dfs(floor, chance ):
    global answer
    if floor == 0: 
        answer = min(floor, answer)
        return None
    
    dfs(floor=floor - 1, chance=chance+1)
    dfs(floor=floor + 1, chance=chance+1)
    dfs(floor=floor - 10, chance=chance+1)
    dfs(floor=floor + 10, chance=chance+1)
    dfs(floor=floor - 1, chance=chance+1)