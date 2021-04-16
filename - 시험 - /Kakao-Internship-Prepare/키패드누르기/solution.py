#%%
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = "LRLLLRLLRRL"

# %%
def getDistance(L, R, number)-> tuple:
    table = {
        '1': [1,1],
        '2': [1,2],
        '3': [1,3],
        '4': [2,1],
        '5': [2,2],
        '6': [2,3],
        '7': [3,1],
        '8': [3,2],
        '9': [3,3],
        '#': [4,1],
        '0': [4,2],
        '*': [4,3]
    }
    number = str(number)
    L = str(L)
    R = str(R)

    num_row, num_col = table[number]
    left_row, left_col = table[L]
    right_row, right_col = table[R]

    left_dist = abs(num_row-left_row)+abs(num_col-left_col)
    right_dist = abs(num_row-right_row)+abs(num_col-right_col)

    return left_dist, right_dist
#%%

def solution(numbers, hand):
    answer = []
    left_loc = '*'
    right_loc = '#'

    left_side = [1,4,7]
    right_side = [3,6,9]


    for number in numbers:
        if number in left_side:
            answer.append('L')
            left_loc = (number)
        elif number in right_side:
            answer.append('R')
            right_loc = (number)
        else:
            left_dist, right_dist = getDistance(left_loc, right_loc, number)
            if left_dist < right_dist:
                answer.append('L')
                left_loc = (number)
            elif left_dist > right_dist:
                answer.append('R')
                right_loc = (number)
            else:
                if hand == 'left':
                    answer.append('L')
                    left_loc = (number)
                else:
                    answer.append('R')
                    right_loc = (number)

    return "".join(answer)


solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2], "left")

# %%
