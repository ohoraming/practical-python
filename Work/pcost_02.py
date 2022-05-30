# pcost.py
#
# Exercise 1.30
"""
연습 문제 1.30: 스크립트를 함수로 탈바꿈

연습 문제 1.27의 pcost.py 프로그램 코드를 가져다가 portfolio_cost(filename) 함수를 만들어 보라. 이 함수는 파일명을 입력으로 받아 포트폴리오 데이터를 읽고, 포트폴리오의 총 비용을 부동소수점으로 반환한다.
"""
def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
        total_cost = 0
        for line in f:
            row = line.split(',')
            shares = int(row[1])
            price = float(row[2])
            total_cost += shares * price
    return total_cost

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')

