"""
제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
"""


"""
participant	completion	return
["leo", "kiki", "eden"]	 ->    ["eden", "kiki"]	-> "leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	  ->   ["josipa", "filipa", "marina", "nikola"]	-> "vinko"
["mislav", "stanko", "mislav", "ana"]	->     ["stanko", "ana", "mislav"]	"mislav"

"""
#%%
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


from collections import Counter


def solution(participant: list[str], completion: list[str]):
    people = Counter(participant)

    for com in completion:
        if com in people:
            people[com] -= 1
    return [k for k, v in people.items() if v]


solution(participant=participant, completion=completion)

# %%
