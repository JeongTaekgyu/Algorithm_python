def solution(str):

    nums = ['0','1','2','3','4','5','6','7','8','9']
    words = ['zero','one','two','three','four','five','six','seven','eight','nine']

    for i in range(len(nums)):
        str = str.replace(words[i], nums[i])

    return int(str)

s = "23four5six7sixsix"
print(solution(s))