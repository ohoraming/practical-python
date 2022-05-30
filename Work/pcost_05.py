# pcost.py
#
# Exercise 1.33
"""
연습 문제 1.33: 명령행에서 읽기

스크립트의 인자로 파일명을 전달하라.
"""
import csv
import sys

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

if len(sys.argv) == 2:
    filename = sys.argv[1]
    print(sys.argv)
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print('Total cost', cost)

"""
명령행에서 전달받은 인자가 있는 경우 sys.argv 리스트에 들어 있다.
(
    참고로, 
    print(sys.argv) 해보면,
    ['pcost_05.py', 'Data/missing.csv']
)
따라서, 이 프로그램은 다음과 같이 터미널에서 실행해야 한다.
$ python pcost_05.py Data/missing.csv

ValueError! ['MSFT', '', '51.23']
ValueError! ['IBM', '', '70.44']
Total cost 43152.15
"""