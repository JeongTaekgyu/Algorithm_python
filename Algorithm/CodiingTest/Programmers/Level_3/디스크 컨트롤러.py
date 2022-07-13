def solution(jobs):
    answer = 0
    start = 0
    length = len(jobs)

    jobs = sorted(jobs, key=lambda x: x[1])
    print(jobs)

    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                break
            # 해당시점에 아직 작업이 들어오지 않았으면 시간 ++
            if i == len(jobs) - 1:
                start += 1

    print('ans : ', answer)
    return answer // length


jobs = [[0, 3], [10,4], [2,5]]
# jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))