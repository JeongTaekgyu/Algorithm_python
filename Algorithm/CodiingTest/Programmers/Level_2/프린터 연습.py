def solution(priorities, location):
    answer = 0
    queue = [(i,p) for i,p in enumerate(priorities)]
    cnt = 1

    while queue:
        job = queue.pop(0)

        if any(job[1] < other_job[1] for other_job in queue):
            queue.append(job)
        else:
            if location == job[0]:
                answer = cnt
                break
            cnt +=1

    return answer


properties = [2, 1, 3, 2]
location = 2
print(solution(properties,location))