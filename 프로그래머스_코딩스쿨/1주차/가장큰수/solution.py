#%%
numbers = [3, 30, 34, 5, 9]


def solution(numbers):
    numbers = list(map(str, numbers))

    def comparison(number: str):
        number = number.ljust(5, "0")
        print(number)
        return (number[0], number[1])

    numbers.sort(key=comparison, reverse=True)
    return "".join(numbers)


solution(numbers)
# %%
