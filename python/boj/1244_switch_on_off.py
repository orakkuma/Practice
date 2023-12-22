n = int(input()) # number of switches
switches = list(map(int, input().split()))

student_cnt = int(input())
for _ in range(student_cnt):
    gender, num = map(int, input().split())

    # 남학생일 때
    if gender == 1:
        #num의 배수들을 모두 바꾼다.
        for i in range(n // num):
            if switches[(i + 1) * num - 1] == 0:
                switches[(i + 1) * num - 1] = 1
            elif switches[(i + 1) * num - 1] == 1:
                switches[(i + 1) * num - 1] = 0



    #여학생일 때
    else:
        #num을 바꾸고, 좌우 대칭일 경우 하나씩 늘언며 바꾼다.
        #단 대칭이 아니거나, 0 <= idx < N일경우 그만둔다.

        if switches[num - 1] == 0:
            switches[num - 1] = 1
        elif switches[num - 1] == 1:
            switches[num - 1] = 0

        j = 1
        while num - 1 - j >= 0 and num - 1 + j < n and switches[num - 1 - j] == switches[num - 1 + j]:
            if switches[num - 1 - j] == 0:
                switches[num - 1 - j] = 1
                switches[num - 1 + j] = 1
            elif switches[num - 1 - j] == 1:
                switches[num - 1 - j] = 0
                switches[num - 1 + j] = 0
            # switches[num - 1 - j] = 1 - switches[num - 1 - j]
            # switches[num - 1 + j] = 1 - switches[num - 1 + j]
            j += 1


    result = []
    for idx, k in enumerate(switches):
        if (idx + 1) % 20 == 1:  # 각 줄의 첫 번째 값은 공백 없이 추가됩니다.
            result.append(str(k))
        else:
            result.append(f' {k}')  # 나머지 값들은 앞에 공백을 붙여서 추가됩니다.
        if (idx + 1) % 20 == 0:  # 20개씩 출력하므로, 20번째 값 뒤에는 줄바꿈을 추가합니다.
            result.append('\n')


print(''.join(map(str, result)))

# 8
# 0 1 0 1 0 0 0 1
# 2
# 1 3
# 2 3



# 강사님 풀이

n = int(input()) # number of switches
switches = list(map(int, input().split()))

student_cnt = int(input())
for _ in range(student_cnt):
    gender, no = map(int, input().split())

    # 스위치 index는 받은 no - 1 이다.
    idx = no - 1

    if gender == 1:

        # idx 가 총 스위치 개수보다 작으면 반복
        while idx < n:
            # 스위치를 바꾼다.(켜져있으면 끄고 / 꺼져있으면 킨다)
            switches[idx] = 0 if switches[idx] == 1 else 1
            # 배수 처리
            idx += no

    else:
        switches[idx] = 0 if switches[idx] else 1
        # = switches[idx] ^= 1
        side = 1
        # idx-side => 왼 / idx+side => 오  가 범위 안에 있고
        while 0 <= (idx -side) and (idx + side) < n:
            l_idx = idx - side
            r_idx = idx + side
            # L == R 일때만 넘어가기
            if switches[idx-side] == switches[idx+side]:
                switches[idx-side] = 0 if switches[idx-side] else 1
                switches[idx+side] = 0 if switches[idx+side] else 1
                # switches[l_idx] ^= 1
                # switches[r_idx] ^= 1
                side += 1
            # L != R 라면 그만
            else:
                break

for line_no in range(n // 20 + 1):
    start = line_no * 20
    end = (line_no + 1) * 20
    print(' '.join(map(str, switches[start:end])))
