# mortgage.py
#
# Exercise 1.11
"""
연습 문제 1.11: 보너스
마지막 달에 초과 납부하는 금액이 생기지 않게 프로그램을 수정해 보라.
"""
extra_payment_start_month = 61 # 5 * 12 = 60
extra_payment_end_month = 108 # 4 * 12 = 48
extra_payment = 1000

principal = 500000.0 # 원금
rate = 0.05 # 연이율
payment = 2684.11 # 월납부금
total_paid = 0.0 # 총 지불금

month = 0

while principal > payment:
    month += 1
    principal = principal * (1 + rate/12) - payment
    total_paid += payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal -= extra_payment
        total_paid += extra_payment
    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Month', month)

"""
1 2684.11 499399.22
2 5368.22 498795.94
3 8052.33 498190.15
...
308 874705.88 3478.83
309 877389.99 809.21
Total paid 877389.99
Month 309
"""