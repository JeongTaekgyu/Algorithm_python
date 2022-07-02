def solution(priorities, location):
    answer = 0
    # 1.queue를 만든다.
    # priorities의 인덱스를 i에 담고 값을 p에 담아라
    queue = [(i,p) for i,p in enumerate(priorities)]
    turn = 0
    print(queue)

    while queue:
        job = queue.pop(0)
        # queue 에 나보다 중요한게 하나라도 있다면
        # 2. 나보다 중요한 job이 있으면 뒤에 넣는다.
        # 참고로 any함수는 인자로 받은 반복가능한 자료형(iterable)중 하나라도 True가 있으면 참(True)을 반환하는 함수이다.
        if any(job[1] < other_job[1] for other_job in queue):
            queue.append(job)
        else:
            turn +=1
            if job[0] == location:
                break
    # 3. 내가 제일 중요하다면 수행하고 location과 비교한다.
    answer = turn

    return answer

priorities = [2,1,2,4,3]
location = 0
print(solution(priorities, location))