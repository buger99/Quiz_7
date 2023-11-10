# 중복이 없는 1부터 45사이의 6개 랜덤번호 생성
import random
lotto_number = []

for i in range(6):
    number = random.randint(1,45)
    lotto_number.append(number)

if number in lotto_number: # 중복이 있는지 없는지 확인
    print("lotto_number에 해당 숫자가 있습니다.")

lotto_number.sort() # 로또번호 정렬
print(lotto_number)

print("생성된 로또 번호는", lotto_number,"입니다.")

# 로또 중복이 있는지 확인하는 코드를 짜는 부분을 모르겠습니다
# 코드를 실행시키면 로또번호엔 중복이 가끔 포함되어 나옵니다
# 게다가 결과값엔 "lotto_number에 해당 숫자가 있습니다" 해당부분이 포함되어 나옵니다.
# 위 내용을 다음주 수업시간에 질문드리고 싶습니다.
