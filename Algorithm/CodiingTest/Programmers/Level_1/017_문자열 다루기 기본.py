def solution(s):
    #    for i in range(len(s)):
    #        print(i)

    if len(s) != 4 and len(s) != 6:
        return False

# 방법1
#    for char in s:
#        if not char.isdigit():
#            return False
# 방법2
#    for char in s:
#        if not (char >= '0' and char <= '9'):
#            return False

# 방법3
    for char in s:
        if not (ord(char) >= 48 and ord(char) <= 57):
            return False

    return True


print(solution('1b34'))
