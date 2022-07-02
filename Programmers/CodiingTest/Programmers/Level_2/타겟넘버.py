# def solution(numbers, target):
#     answer = 0
#     depth = 0
#
#     def dfs(numbers, target, sum, depth):
#         if depth == len(numbers):
#             if sum == target:
#                 nonlocal answer
#                 answer += 1
#             return
#
#         dfs(numbers, target, sum + numbers[depth], depth + 1)
#         dfs(numbers, target, sum - numbers[depth], depth + 1)
#
#     dfs(numbers, target, 0, depth)
#
#     return answer

#from collections import deque


# def solution(numbers, target):
#     answer = 0
#     queue = deque()  # queue 생성
#
#     length = len(numbers)
#     queue.append([-numbers[0], 0])
#     queue.append([+numbers[0], 0])
#
#     print(queue)
#
#     while queue:
#         num, i = queue.popleft()
#         print('num : ', num, ',  i : ', i)
#         if i + 1 == length:
#             if num == target:
#                 answer += 1
#         else:
#             queue.append([num - numbers[i + 1], i + 1])
#             queue.append([num + numbers[i + 1], i + 1])
#
#     return answer

# stack을 이용한 dfs여도 마찬가지!
def solution(numbers, target):
    answer = 0
    queue = [[numbers[0],0], [-1*numbers[0],0]]
    n = len(numbers)
    while queue:
        temp, idx = queue.pop()
        idx += 1
        if idx < n:
            queue.append([temp+numbers[idx], idx])
            queue.append([temp-numbers[idx], idx])
        else:
            if temp == target:
                answer += 1
    return answer

numbers = [4, 1, 2, 1]
target = 4
print(solution(numbers, target))