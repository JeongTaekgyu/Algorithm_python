def solution(phone_number):
    phone_number_len = len(phone_number)

    answer = '*' * (phone_number_len-4)

    answer += phone_number[-4:] # 뒤에서 원하는 글자수 만큼 잘라서 answer 뒤에 붙이기
    return answer

print(solution("01033324744"))