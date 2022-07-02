input = [4, 6, 2, 9, 1]

# 삽입정렬 ex) 전체에서 최소값을 선택해서 앞쪽으로 가져온다.
def selection_sort(array):

    size = len(array)

    n = len(array)
    for i in range(n - 1):
        print(i ,"----")
        min_index = i
        for j in range(n - i):
            print(i + j)
            if array[i + j] < array[min_index]:
                min_index = i + j

        array[i], array[min_index] = array[min_index], array[i]

    return array


selection_sort(input)
print(input) # [1, 2, 4, 6, 9] 가 되어야 합니다!