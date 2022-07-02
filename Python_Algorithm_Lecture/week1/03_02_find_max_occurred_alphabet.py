input = "hello xxmyx name is spartaxxx"


def find_max_occurred_alphabet(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    # 가장 많이 발생했던 빈도수
    max_occurrence = 0
    # 가장 많이 발생했던 알파벳의 인덱스
    max_alphabet_index = 0

    print("------------", range(len(alphabet_occurrence_array)))
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence > max_occurrence:
            max_alphabet_index = index
            max_occurrence = alphabet_occurrence

    print(ord("a"))         # char to ascii code
    print(chr(ord("a")))    # number to char

    print("max_alphabet_index : ", max_alphabet_index)   # 최빈값의 index
    print("ord(\"a\") : ", ord("a") )
    print("chr(숫자) : ", chr(100))
    return chr(max_alphabet_index + ord("a"))   # 최빈값 alphabet

    # # char를 ascii 코드로(number로)
    # a -> 0
    # a -> ord(a) -> 97 - ord(a) = 0
    #
    # # number를 char로
    # 0 -> a
    # 0 -> 0 + ord(a) -> 97 -> char(97) -> a

    return alphabet_occurrence_array


result = find_max_occurred_alphabet(input)
print("최빈값 앞파벳 : ", result)
