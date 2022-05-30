# pcost.py
#
# Exercise 1.32
"""
연습 문제 1.32: 라이브러리 함수 사용하기

csv 모듈을 사용해 파싱을 하도록 pcost_03.py 프로그램을 수정한 다음, 이전의 예제를 실행해보라.
"""
import csv

def portfolio_cost(filename):
    with open(filename) as f:
        lines = csv.reader(f)
        headers = next(lines)
        total_cost = 0

        for line in lines:
            try:
                shares = int(line[1])
                price = float(line[2])
            except ValueError:
                print("ValueError!", line)
            total_cost += shares * price
    return total_cost

cost = portfolio_cost('Data/missing.csv')
# cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost}')

