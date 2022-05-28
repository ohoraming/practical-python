# mortgage.py
#
# Exercise 1.8
"""
연습 문제 1.8: 추가 납입
데이브가 처음 12개월 동안 매달 1000 달러를 추가로 납입한다면 어떻게 될까?

이 추가 납입금 계산을 포함하도록 프로그램을 수정해 총 납입금액과 소요 월수를 프린트해보자.

프로그램을 실행했을 때 총 납입금이 929,965.62, 소요 월수는 342로 나와야 한다.
"""
principal = 500000.0 # 원금
rate = 0.05 # 연이율
payment = 2684.11 # 월납부금
total_paid = 0.0 # 총 지불금

month = 0

while principal > 0:
    month += 1
    principal = principal * (1 + rate/12) - payment
    total_paid += payment

    if month >= 1 and month <= 12:
        principal -= 1000
        total_paid += 1000
    
    print(month, total_paid)

print('Total paid', round(total_paid, 2))

"""
1 3684.11
2 7368.22
3 11052.33
...
341 927281.5099999959
342 929965.6199999959
Total paid 929965.62
"""