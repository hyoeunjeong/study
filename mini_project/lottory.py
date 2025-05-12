
import random

print("💲💲Welcom💲💲")
print("로또 번호 랜덤 프로그램에 오신 여러분 환영합니다.😁")
print("여러분의 운세는 인생역전 인가요 인생 여전인가요?? ")
print("🤞행운을 빕니다.🤞")


def generate_lotto_numbers():
     lotto_numbers = random.sample(range(1, 46), 6)  #1~45 중 6개 
     lotto_numbers.sort()  # 번호를 정렬하기
     return lotto_numbers


recommended_numbers = generate_lotto_numbers()
print("추천 번호:", recommended_numbers)



