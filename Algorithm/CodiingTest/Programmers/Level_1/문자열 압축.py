def solution(s):
    answer = len(s)

    for i in range(1, (len(s) // 2) + 1):   # len(s) // 2 까지 포함돼서 반복해야 해서 +1 해준다.
        pos = 0 # position
        # 길이만 필요하다
        length = len(s)

        while pos + i <= len(s):
            unit = s[pos:pos+i]
            pos += i    # 읽어온 만큼 위치를 변경?

            while pos + i <= len(s):
                if unit == s[pos:pos+i]


    return answer


s = "ababcdcdababcdcd"
print(solution(s))