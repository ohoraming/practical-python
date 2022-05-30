# pcost.py
#
# Exercise 1.27
"""
연습 문제 1.27: 데이터 파일 읽기
파일을 읽는 방법을 알았으니 간단한 계산을 수행하는 프로그램을 작성하자.

portfolio.csv의 각 컬럼은 보유 종목의 이름, 주식 수, 매수가격에 해당한다. 이 파일을 열어 전체 행을 읽은 뒤, 포트폴리오의 전체 주식을 매수하는 데 드는 비용을 계산하는 pcost.py 프로그램을 작성한다.

힌트: 문자열을 정수로 변환하려면 int(s)를 사용한다. 문자열을 부동소수점으로 변환하려면 float(s)를 사용한다.

다음과 같이 출력하는 프로그램을 작성하라.

Total cost 44671.15
"""
total_cost = 0
f = open('Data/portfolio.csv', 'rt')
next(f)
for line in f:
    row = line.split(',')
    total_cost += int(row[1]) * float(row[2])
f.close()

print(f'Total cost {total_cost}')

"""
Total cost 44671.15
"""
