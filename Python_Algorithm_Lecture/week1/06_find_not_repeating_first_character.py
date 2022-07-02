input = "abadabac"

def find_not_repeating_first_character(string):
    alphabet_occurrence_array = [0] * 26

    # 이 부분을 채워보세요!
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord("a")
        alphabet_occurrence_array[arr_index] += 1

    # 반복되지 않는 문자
    not_repeating_character_array = []
    for index in range(len(alphabet_occurrence_array)):
        alphabet_occurrence = alphabet_occurrence_array[index]

        if alphabet_occurrence == 1:    # 하나만 나오면 반복이 안되니까
            not_repeating_character_array.append( chr(index + ord("a")) )

    print("---- : ", not_repeating_character_array)

    for char in string:
        # ★★★ not_repeating_character_array 안에 char 가 있다면
        if char in not_repeating_character_array:
            return char

    return "_"


result = find_not_repeating_first_character
print("정답 = d 현재 풀이 값 =", result("abadabac"))
print("정답 = c 현재 풀이 값 =", result("axabbcddmd"))
print("정답 =_ 현재 풀이 값 =", result("aaaaaaaa"))