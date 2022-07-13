def solution(numbers):
    answer = 45

    for num in numbers:
        answer -= num

    return answer
    # 아래 것 만으로 답이 됨 애초에 array를 sum 해주는 함수가 있네요 ㄷㄷ
    #return 45 - sum(numbers) 

array = [1,2,3,4,6,7,8,0]
print(solution(array))