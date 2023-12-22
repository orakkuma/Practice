def solution(d, budget):
    d.sort()

    total = 0
    answer = 0

    for don in d:
        total += don
        if total > budget:
            break
        answer += 1
    return answer


print(solution([1,3,2,5,4], 9))  # 3
print(solution([2,2,3,3], 10))   # 4


#강사님 풀이
# def solution(d, budget):
#     d.sort()
#     answer = 0
#     for n in d:
#         budget -= n
#         if budget >= 0:
#             answer += 1
#         else:
#             break
#     return answer
# print(solution([1,3,2,5,4], 9))  # 3
# print(solution([2,2,3,3], 10))   # 4