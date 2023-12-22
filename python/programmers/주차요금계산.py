# def solution(fees, records):
#     answer = []
#     # 입력값
#     # 기본시간, 기본요금, 요금추가될 단위시간(분), 단위요금
#     stt, stm, unitmin, unitmoney = map(int, input().split())
#
#     records = input()
#     car_num = []
#     for idx in input:
#         for num in idx:
#
#
#
#
#
#
#
#
#     return answer


from collections import defaultdict
import math


def solution(fees, records):
    base_time, base_fee, unit_time, unit_fee = fees
    parking_times = defaultdict(int)
    in_records = {}

    def calculateFee(parking_time):
        if parking_time <= base_time:
            return base_fee
        else:
            extra_time = parking_time - base_time
            return base_fee + math.ceil(extra_time / unit_time) * unit_fee

    for record in records:
        time, car, action = record.split()
        hh, mm = map(int, time.split(':'))
        minutes = hh * 60 + mm

        if action == "IN":
            in_records[car] = minutes
        else:  # OUT
            parking_time = minutes - in_records.pop(car)
            parking_times[car] += parking_time

    for car, entry_time in in_records.items():
        parking_time = 23 * 60 + 59 - entry_time
        parking_times[car] += parking_time

    fees = {}
    for car, time in parking_times.items():
        fees[car] = calculateFee(time)

    sorted_fees = [fees[key] for key in sorted(fees.keys())]
    return sorted_fees


# 입력값과 출력 예시
fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT",
    "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN",
    "23:00 5961 OUT"
]

# 함수 실행 및 결과 출력
result = solution(fees, records)
print(result)
