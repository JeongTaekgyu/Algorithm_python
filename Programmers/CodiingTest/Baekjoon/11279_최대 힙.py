from sys import stdin

def deleteHeap(num, curIdx):

    queue[curIdx], queue[1] = queue[1], queue[curIdx]
    maxValue = queue.pop()
    print(maxValue)

    curIdx = 1
    while curIdx <= len(queue) -1:
        L_childIdx = curIdx * 2
        R_childIdx = curIdx * 2 + 1
        maxIx = curIdx




def insertHeap(num, curIdx):

    while curIdx > 1:
        parent_dix = curIdx // 2
        if queue[curIdx] > queue[parent_dix]:
            queue[curIdx], queue[parent_dix] = queue[parent_dix], queue[curIdx]
            curIdx = parent_dix
        else:
            break

n = int(stdin.readline())
queue = [0]

print(queue)

for i in range(n):
    num = int(stdin.readline())
    queue.append(num)
    curIdx = len(queue) - 1

    if num == 0:
        deleteHeap(num, curIdx)

    insertHeap(num, curIdx)


print(queue)
