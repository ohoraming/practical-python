# pcost.py
#
# Exercise 1.31
"""
연습 문제 1.31: 오류 처리

오류를 잡아서 경고 메시지를 프린트하고, 파일의 끝까지 계속 처리하게 pcost_03.py 프로그램을 수정해 보자.
"""
def portfolio_cost(filename):
    with open(filename, 'rt') as f:
        headers = next(f)
        total_cost = 0
        for line in f:
            row = line.split(',')
            try:
                shares = int(row[1])
                price = float(row[2])
            except ValueError:
                print("ValueError!", line)
            total_cost += shares * price
    return total_cost

cost = portfolio_cost('Data/missing.csv')
print(f'Total cost: {cost}')

