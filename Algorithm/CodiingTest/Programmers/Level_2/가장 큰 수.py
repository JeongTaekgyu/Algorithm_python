def solution(numbers):
    #0. key point
    numbers_str = [str(num) for num in numbers]                 #1. String 형으로 사전 값으로 정렬하기
    print('~0 : ', numbers_str)
    numbers_str.sort(key=lambda num: num*3, reverse=True)       #2. number는 1000이하의 숫자이므로 x3(반복)한 값으로 비교
    # key는 key값을 기준으로 정렬된다.

    print('~1 : ', list(map(lambda x: x*3 , numbers_str)))
    # 999, 555, 343434, 333, 303030

    print('numbers_str : ' , numbers_str)

    return str(int(''.join(numbers_str)))
    # 만약 numbers=[0,0,0,0] 이라면 0 이 나와야 한다.
    # join한 값을 int로 만들어 준 후 원하는 return값이 str이기 때문에 다시 str로 변환한다.

print(solution([6, 10, 2]))             # result : 6210
print(solution([3, 30, 34, 5, 9]))      # result : 9534330
print(solution([0,0,0,0]))              # result : 0
print(solution([2,7,14,36]))