# mortgage.py
#
# Exercise 1.9
"""
연습 문제 1.9: 추가 납입금 계산기
추가 납입금을 일반적으로 다룰 수 있게 프로그램을 수정하자. 사용자가 다음 변수를 설정할 수 있게 한다.
"""
extra_payment_start_month = 61 # 5 * 12 = 60
extra_payment_end_month = 108 # 4 * 12 = 48
extra_payment = 1000

"""
프로그램이 이 변숫값을 읽고 총 납입액을 계산하게 해 보자.

데이브가 대출 시작 5년 후부터 4년간 매달 1000 달러를 추가로 지불할 경우 총 납입액은 얼마인가?
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

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    print(month, total_paid)

print('Total paid', round(total_paid, 2))

"""
1 2684.11
2 5368.22
3 8052.33
...
309 877389.9899999964
310 880074.0999999964
Total paid 880074.1
"""