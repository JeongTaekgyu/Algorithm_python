import math

def solution(numbers, hand):
    answer = ''

    dic = {
        1:[0,0], 2:[1,0],  3:[2,0],
        4:[0,1], 5:[1,1],  6:[2,1],
        7:[0,2], 8:[1,2],  9:[2,2],
      '*':[0,3], 0:[1,3],'#':[2,3]
    }

    LeftHandPos = dic['*']
    RightHandPos = dic['#']

    for num in numbers:
        if num in [1,4,7]:
            answer += 'L'
            LeftHandPos = dic[num]
        elif num in [3,6,9]:
            answer += 'R'
            RightHandPos = dic[num]
        else:
            a = abs(LeftHandPos[0] - dic[num][0])
            b = abs(LeftHandPos[1] - dic[num][1])
            ld = a + b
            # a = LeftHandPos[0] - dic[num][0]
            # b = LeftHandPos[1] - dic[num][1]
            # ld = math.sqrt((a * a) + (b * b))

            c = abs(RightHandPos[0] - dic[num][0])
            d = abs(RightHandPos[1] - dic[num][1])
            rd = c + d
            # c = LeftHandPos[0] - dic[num][0]
            # d = LeftHandPos[1] - dic[num][1]
            # rd = math.sqrt((c * c) + (d * d))

            if ld < rd:
                answer += 'L'
                LeftHandPos = dic[num]
            elif ld > rd:
                answer += 'R'
                RightHandPos = dic[num]
            else: # lc == rc
                if hand == 'left':
                    answer += 'L'
                    LeftHandPos = dic[num]
                elif hand == 'right':
                    answer += 'R'
                    RightHandPos = dic[num]

    return answer

# 시작 위치만 왼손 '*, 오른손 '#' 이고 그 이후엔 터치를 안한다.
numbers = [0,8,5,0,0,8,0,8,8]
hand = "right"
print(solution(numbers, hand))