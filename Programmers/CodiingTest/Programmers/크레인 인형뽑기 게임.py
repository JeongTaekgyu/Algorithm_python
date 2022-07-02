def solution(board, moves):
    answer = 0
    bucket = []

    for value in moves:
        for i in range(len(board)):
            if board[i][value - 1] > 0:
                bucket.append(board[i][value-1])    # i가 행이군
                board[i][value - 1] = 0
                if bucket[-1:] == bucket[-2:-1]:    # 맨 위에거랑 맨뒤에서 2번째거가 같으면
                    answer += 2     # 2개 터짐
                    bucket = bucket[:-2]    # 터졌으니까 맨 뒤 2개 제외한걸 담는다.
                # 맨뒤랑 맨뒤에서 두번째 인형이 같지 않으면 break 해서 가장 가까운 for문 탈출
                break

    print(moves[-1:])   # 뒤에서 1번째
    print(moves[:-2])   # 뒤에 2개 제외한 리스트
    print(moves[-2:-1]) # 뒤에서 2번째

    return answer


board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))