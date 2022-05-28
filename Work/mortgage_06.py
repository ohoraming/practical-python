# mortgage.py
#
# Exercise 1.17
"""
연습 문제 1.17: f 문자열(f-strings)
연습 문제 1.10의 mortgage.py 프로그램을 수정해, f 문자열을 사용해 출력을 생성하게 해 보자. 출력을 보기 좋게 정렬해보라.
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
    print(f'월수:{month}, 현재까지의 납부액: {round(total_paid, 2)}달러, 남은 원금: {round(principal, 2)}달러')

print(f'Total paid: {round(total_paid, 2)}')
print(f'Month: {month}')

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