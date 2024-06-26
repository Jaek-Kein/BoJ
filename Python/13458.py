#Question no 13458 시험감독
import sys

judge_count = 0

place = int(sys.stdin.readline()) # 시험장의 갯수를 지정

if place == 1:
    tester = int(sys.stdin.readline())  #시험장이 1곳일 경우 단일수 입력
else:
    tester = list(map(int, sys.stdin.readline().split()))   #시험장이 다수일경우 리스트 형태로 입력

main, sub = map(int, sys.stdin.readline().split())  #총감독관과 부감독의 감시가능 학생수를 map(split)으로 지정

if place == 1: # 장소가 한곳일 경우의 코드
    tester -= main
    judge_count += 1    # 총감독관은 시험장당 1명 뿐이기에 단일계산으로 배고 시작
    if tester > 0:
        judge_count += tester//sub
        if tester%sub != False:
            judge_count += 1
else:
    for i in tester :
        i -= main
        judge_count += 1
        if i > 0:
            judge_count += i//sub
            if i%sub != False:
                judge_count += 1
        else:
            continue

print(judge_count)
