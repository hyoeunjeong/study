## 효은이의 두번째 미니 프로젝트 (식사메뉴 추천 프로그램)
import random
recommendationse ={"한식":["김치찌개","닭도리탕","갈치조림","갈비찜","냉면","백반"],
                   "중식":["탕수육","마라탕","마라샹궈","짬뽕","짜장면","칠리새우","양장피"],
                   "일식":["초밥","소바","라멘","오코노미야끼","우동","돈까스","야끼소바"],
                   "고기":["삼겹살","갈비","등심","항정살","갈매기살","목살","안심"],
                   "야식":["닭발","족발","오돌뼈","보쌈","떡볶이","찜닭","야채곱창"],
                   "치킨":["황금올리브","뿌링클","허니오리지널","슈프림치킨","레드콤보","핫후라이드","마늘 통닭"],
                   "피자":["고구마 피자","치즈피자","페퍼로니피자","하와이안 피자","포테이토 피자","콤비네이션 피자"],
                   "편의점":["편의점 도시락","컵라면","닭가슴살","핫바","과자","삼각김밥","샌드위치"]}

while True :
 print("🍴어서오세요 맛잘알 추천기 입니다.🍴")
 print("👉 선택 가능한 음식 종류:")
 for kind in recommendationse:
    print(f"{kind}")

 user_choice =input("🤤땡기는음식을 선택하시오🤤 ")
 if user_choice in recommendationse:
    menu = random.choice(recommendationse[user_choice]) 
    print(f"{user_choice} 중  식사메뉴는  🤤두구구두구🤤")
    print(f"{menu}")
  
 #for menu in recommendationse[user_choice]:
    
  #  print(f"👉 오늘의 추천 메뉴{menu}")

 else: 
    print("⚠️ 존재하지 않는 음식 종류입니다. 다시 입력해주세요 ")

 print("프로그램 종류를 원하시면 0 번을 계속하시기를 원한다면 1번을 누루시오")
 number = input()
 if number == "0":
    print("👋 프로그램을 종료합니다. 맛있게 드세요!")
    break
 elif number == "1" :
   print(" 🍽 다시 추천을 시작합니다!")
 else:
   print("❗ 잘못된 입력입니다❗ 계속 진행합니다")