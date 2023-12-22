# def solution(s):
#
#     s_list = s.split()
#     answer = []
#
#     for word in s_list:
#         sumchars = ''
#
#         for i,char in enumerate(word):
#             if i % 2 == 0:
#                 sumchars += char.upper()
#             else:
#                 sumchars += char.lower()
#
#         answer.append(sumchars)
#     return ' '.join(answer)
#
#
# print(solution("try hello world")) # "TrY HeLlo WoRlD"
# print(solution("What are you going to do"))
# print(solution("I was the only one who didn’t know"))
# print(solution("Please take me to the mart on the way to the hospital"))

# 내가 풀었는데 예외 때문에 통과 못 한 코드
# def solution(s):
#
#     s_list = s.split()
#     answer = []
#
#     for word in s_list:
#         words = ''
#
#         for i in range(len(word)):
#             if i % 2 == 0:
#                 words += word[i].upper()
#             else:
#                 words += word[i].lower()
#
#         answer.append(words)
#     return ' '.join(answer)
#
#
# print(solution("try hello world")) # "TrY HeLlo WoRlD"


#강사님 풀이
# def solution(s):
#     words = s.split()
#     new_words = []
#     for word in words:
#         new_word = ''
#         for idx, char in enumerate(word):
#             if idx % 2 == 0:
#                 new_word += char.upper()
#             else:
#                 new_word += char.lower()
#         new_words.append(new_word)
#
#     return ' '.join(new_words)
#
#
# print(solution("try hello world"))  # "TrY HeLlo WoRlD"

def solution(s):
    idx = 0
    new_str = ''

    for char in s:
        # 공백문자일 경우 그대로 넣고 짝/홀 판별 idx 리셋
        if char == ' ':
            new_str += char
            idx = 0
            continue

        elif idx % 2:
            new_str += char.lower()

        elif idx % 2 == 0:
            new_str += char.upper()

        idx += 1
    return new_str

print(solution("try hello world"))  # "TrY HeLlo WoRlD"