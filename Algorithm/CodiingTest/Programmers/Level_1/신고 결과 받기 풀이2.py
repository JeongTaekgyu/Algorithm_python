# 한 유저가 같은 유저를 여러 번 신고한 경우는
# 신고 횟수 1회로 처리하기 때문에 set을 사용한다.
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    reports = {x : 0 for x in id_list}  # x인 key는 id_list 안에 있는 값이 되고 value는 0으로 통일됨
    # reports는 딕셔너리 형태로 만든다.
    print('reports : ', reports)
    print(reports['apeach'])
    print(id_list.index('apeach'))

    for r in set(report):   # set을 사용했다.(유저가 같은 유저를 여러 번 신고한 경우는 신고 횟수 1회로 처리 해서)
        #print("r : ",r)
        print(r.split()[0], r.split()[1])
        reports[r.split()[1]] += 1  # 신고 당한놈 +1
    # 위에 for문이 끝나면 reposts는 key: value = 신고당한 놈 : 횟수 가 들어있음
    print(reports)

    for r in set(report):
        if reports[r.split()[1]] >= k:  # 신고 당한놈이 k번 이상 신고 당했으면
            # id_list에 사용자 이름이 key인 인덱스인데 그 인덱스를 answer의 인덱스에 있는 값을 +1 한다.
            # ( id_list에 있는 사용자가 신고한 사용자(신고당한 사용자)가 k번 이상 신고를 당했으면 메일을 보내줘야하니까 )
            answer[id_list.index(r.split()[0])] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]    # 조건이 id_list에 있는 값은 중복 되면 안됨
report = ["muzi frodo", "muzi frodo","apeach frodo",
          "frodo neo","muzi neo","apeach muzi", "apeach frodo"]
k = 2
print(solution(id_list, report, k))