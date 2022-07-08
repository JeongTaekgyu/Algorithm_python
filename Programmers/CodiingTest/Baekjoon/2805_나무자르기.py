N, M = map(int, input().split())
woodList = list(map(int, input().split()))  # 배열에 입력받기
start = 1
end = max(woodList)

while start <= end:
    mid = (start + end) // 2
    amount = 0

    for wood in woodList:
        if wood > mid:
            amount += wood - mid

    if amount >= M:
        start = mid + 1
    else:
        end = mid - 1

print(end)