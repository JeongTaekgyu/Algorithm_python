def solution(arr):
#    answer = min(arr)   # 배열에서 min값 찾기
#    answer = max(arr)   # 배열에서 max값 찾기

    if len(arr) == 1:
        return [-1]
    else:
        minNum = min(arr)   # 배열에서 min값을 구한다.
        arr.remove(minNum)
        #arr.pop(arr.index(minNum))  # 배열에서 min값의 인덱스 찾고, 해당 인덱스에 있는 값을 삭제한다.
        return arr

arr = [5,6,3,7,2]
print(solution(arr))