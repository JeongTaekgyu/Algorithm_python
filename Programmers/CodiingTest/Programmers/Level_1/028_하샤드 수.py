def solution(x):

    nlist = list(map(int, str(x)))  # 각 자리수를 리스트로 변환

    if x % sum(nlist) == 0:
        return True
    else:
        return False

print(solution(22))