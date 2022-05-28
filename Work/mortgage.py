# mortgage.py
#
# Exercise 1.7
"""
연습 문제 1.7: 데이브의 주택 담보 대출
데이브는 500,000 달러의 30년 고정 이율 주택 담보 대출(mortgage)을 받기로 결정했다. 이율은 5%이고 매달 납부할 금액은 2684.11 달러다.

다음은 대출 기간 동안 지불할 총액을 계산하는 프로그램이다.
"""
principal = 500000.0 # 원금
rate = 0.05 # 연이율
payment = 2684.11 # 월납부금
total_paid = 0.0 # 총 지불금

while principal > 0:
    principal = principal * (1 + rate/12) - payment
    total_paid += payment

print('Total paid', round(total_paid, 1))

