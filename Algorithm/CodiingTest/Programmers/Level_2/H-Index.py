def solution(citations):
    answer = 0
    citations.sort()
    article_count = len(citations)

    for i in range(article_count):
        if citations[i] >= article_count - i:
            return article_count - i

    # citations.sort()
    # for idx, citation in enumerate(citations):
    #     if citation >= len(citations) - idx :
    #         return len(citations) - idx

    return answer

citations = [3, 0, 6, 1, 5]
#citations = [5, 1, 5, 2, 7, 8, 5]
print(solution(citations))