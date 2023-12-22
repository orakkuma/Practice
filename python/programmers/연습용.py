# 없는숫자 더하기
# def solution(numbers):
#     allnum = range(10)
#     set_allnum = set(allnum)
#     set_num = set(numbers)
#
#     result  = set_allnum - set_num
#     answer = 0
#
#     for i in result:
#         answer += i
#
#     return answer
#
# print(solution([1, 2, 3, 4, 6, 7, 8, 0])) # 14
# print(solution([5, 8, 4, 0, 6, 7, 9])) # 6



#예산
# def solution(d, budget):
#     d.sort()
#
#     result = 0
#     answer = 0
#     for don in d:
#         if result + don <= budget:
#             result += don
#             answer += 1
#         else:
#             break
#
#
#     return answer
#
#
# print(solution([1,3,2,5,4], 9))  # 3
# print(solution([2,2,3,3], 10))   # 4


