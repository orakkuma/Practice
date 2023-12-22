def solution(numbers):
    allnum = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    set_allnum = set(allnum)
    set_numbers = set(numbers)

    result = set_allnum - set_numbers

    answer = 0
    for i in result:
        answer += i

    # answer = -1
    return answer

print(solution([1,2,3,4,6,7,8,0])) # 14
print(solution([5,8,4,0,6,7,9])) # 6


#강사님 풀이
# def solution(numbers):
#
#     allnumbers = list(range(10))
#     for num in numbers:
#         allnumbers.remove(num)
#
#     return sum(allnumbers)
#
# print(solution([1,2,3,4,6,7,8,0])) # 14
# print(solution([5,8,4,0,6,7,9])) # 6

# def solution(numbers):
#     answer = sum(range(10))
#     for num in numbers:
#         answer -= num
#
#     return answer
#
# print(solution([1,2,3,4,6,7,8,0])) # 14
# print(solution([5,8,4,0,6,7,9])) # 6
