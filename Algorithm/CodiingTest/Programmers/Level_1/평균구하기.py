def solution(arr):

    answer = sum(arr) / len(arr)
#    print(f"average : {answer / len(arr)}")
    print("average : ", answer)

    return answer


arr = [1,2,3,4]
print(solution(arr))