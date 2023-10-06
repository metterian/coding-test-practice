#%%
"""
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.

구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421

"""


phone_book = ["12","123","1235","567","88"]# False



#%%
from itertools import combinations


def solution(phone_book):
    phone_book = sorted(phone_book, key= lambda x: len(x))

    for prefix1, prefix2 in combinations(phone_book, 2):
        if prefix2.startwith(prefix1):
            return False
    return True


solution(phone_book=phone_book)
# %%
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        print(p1, p2)


solution(phoneBook=phone_book)
# %%
