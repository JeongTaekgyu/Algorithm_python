def solution(nums):
    answer = 0
    numsSize = len(nums)/2

    numSet = set(nums)
    numSetSize = len(numSet)

    print('len : ', len(nums))
    print('len/2 :' , len(nums)/2)
    print('numSize : ', numsSize)
    print('numSetSize : ', numSetSize)

    if numSetSize < numsSize:
        answer = numSetSize
    else:
        answer = int(numsSize)

    print('min : ', min(len(nums)/2, len(set(nums))) )

    return min(len(nums)/2, len(set(nums)))
    #return answer

nums = [3,3,3,2,2,4,1,3]
print(solution(nums))