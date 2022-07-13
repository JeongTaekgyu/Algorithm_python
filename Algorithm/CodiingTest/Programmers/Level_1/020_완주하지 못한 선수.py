import collections


def solution(participant, completion):

# 풀이1
#    participant.sort()
#    completion.sort()

#    for i in range(len(completion)):
#        if completion[i] != participant[i]:
#            return participant[i]

#    answer = participant[len(completion)]
#    return answer

# 풀이2
    # Counter() : 문자열이나, list 의 요소를 카운팅하여 많은 순으로 딕셔너리형태로 리턴한다
 #   print(collections.Counter(participant))
 #   print(collections.Counter(completion))

#    test = collections.Counter(participant) - collections.Counter(completion)
#    print(test)
#    print("답은 : ", list(test.keys())[0])

#    return list(test.keys())[0]

# dic : participant 딕셔너리 만들기
# participant의 sum(hash)구하기


# 풀이3
    answer = ''
    temp = 0
    dic = {}
    for part in participant:
        dic[hash(part)] = part
        temp += int(hash(part))
        print(hash(part))
        print(dic[hash(part)])
    for com in completion:
        temp -= hash(com)
    answer = dic[temp]

    print("라스트 temp : ",temp)
    return answer


participant = ["leo", "mis", "bb", "taek", "mis"]
completion = ["mis", "taek", "leo", "mis"]

print(solution(participant, completion))