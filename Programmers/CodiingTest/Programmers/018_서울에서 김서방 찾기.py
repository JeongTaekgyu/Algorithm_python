def solution(seoul):
    answer = ''

    # 실행속도 차이난다.
    # 파이썬 따옴표와 쌍따옴표의 차이..
#    - 쌍따옴표("): 진짜 일반적인 문자열에 쓰임
#    - 단따옴표('): 기호나 식별자 define이나 list 정의할때
    
    # 방법1
    idx = seoul.index("Kim")
    answer = '김서방은 ' + str(idx) + '에 있다'

    # 방법2
    #    for i in range(len(seoul)):
    #        if seoul[i] == "Kim":
    #            answer = '김서방은 "+str(i)+"에 있다'
    
    # f str 과 format 방법 !! 알기!

    return answer


arr = ["Jane", "Lee", "Kim", "Man"]
print(solution(arr))
