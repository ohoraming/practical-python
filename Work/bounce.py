# bounce.py
#
# Exercise 1.5
"""
연습 문제 1.5: 얌체공
고무 공을 100미터 높이에서 떨어뜨린다. 이 공은 땅에 닿을 때마다 원래 높이의 3/5만큼 튀어오른다. 공이 열 번 튈 동안, 그때마다 높이를 나타내는 테이블을 프린팅하는 프로그램 bounce.py를 작성하라.
"""
num = 0
height = 100

for i in range(10):
    height *= 3/5
    num += 1
    print(num, round(height, 4))


