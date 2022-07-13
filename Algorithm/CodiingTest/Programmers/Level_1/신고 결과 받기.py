def solution(id_list, report, k):
    answer = [0] * len(id_list)
    report = set(report)    # report의 중복을 없애준다.
    check = {}  # 유저가 몇번 신고 당했는지 저장한 딕셔너리
    lst = {}    # 신고한 유저와 신고당한 유저 딕셔너리

    print('report set : ', report)

    for s in report:
        a, b = s.split(' ')

        if b not in check:
            check[b] = 1
        else:
            check[b] += 1

        if a not in lst:    # 신고한 사람이 lst에 없으면
            lst[a] = [b]    # key(a)에 신고한사람, value(b)에 신고당한 사람을 넣는다.
        else:   # 신고한 사람(a)이 lst에 있고,
            if b not in lst[a]: # 신고 당한 사람(b)이 lst[신고한사람(a)]에 없다면
                lst[a] += [b]   # 신고한 사람(a)이 있는 key에 신고 당한 사람(b)을 넣는다.

    print('check : ', check)
    print('lst : ', lst)


    # 1. check 딕셔너리를 돌면서 신고당한 횟수가 k 번 이상인 유저들을 체크한다.
    # 2. 해당 유저를 신고한 유저들이 받아야 할 메시지 개수를 + 1 해준다.
    for id_, n in check.items():    # items() 함수는 key, value 쌍을 얻는 함수이다.
        if n >= k:
            for user, user2 in lst.items():
                if id_ in user2:    # user2 에 _id(check의 key)가 있다면
                    # 신고한사람(user)이 있는 인덱스에
                    answer[id_list.index(user)] += 1 # 신고한 사람이 받을 메시지 +1 해줌

    print(id_list.index('muzi'))

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi", "apeach frodo"]
k = 2
#print(report[1].split(" ")[1])
print(solution(id_list, report, k))