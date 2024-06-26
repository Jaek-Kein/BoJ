import sys

trial = int(sys.stdin.readline()) # 지정된 시도횟수를 변수로써 지정

while trial != 0:
    a, b = map(int, sys.stdin.readline().split()) # 데이터 수인 a^b 의 각각 a 와 b를 입력받습니다.
    if b%4 == 0: #왜 4로 나누는가?
        exponent = 4 # 문제 제공범위를  보면  0<b<1,000,000 이기에 **연산으로 처리할경우 제한시간을 초과하기에 뒷자리수가 4의배수 지수마다 돌아온다는것을 이용 지수의 크기를 줄여줌
    else:
        exponent = b%4
    if a**exponent%10 == 0:
        print(10)
        trial-=1
    else:
        print(a**exponent%10)
        trial-=1