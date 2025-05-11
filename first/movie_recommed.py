## 효은이의 첫번째 미니 프로젝트 영화 추천프로그램


### 장르별 딕셔너리 key(장르):value(영화)
recommendationse ={"sf":["인터스텔라","마션","인셉션","아바타","에이리언","듄"],
        "공포":["곤지암","장화홍련","컨저링","알포인트","오디션","파라노말 액티비티"],
        "로맨스": ["노트북", "어바웃 타임","말할 수 없는 비밀", "비포 선셋","대도시의 사랑법"],
        "드라마": ["쇼생크 탈출", "포레스트 검프", "그린 마일","올드보이","신세계"],
        "판타지": ["해리 포터", "반지의 제왕", "나니아 연대기","트와일라잇","판의 미로","신비한 동물 사전"],
        "스릴러": ["세븐", "살인의 추억", "겟 아웃","악마를 보았다","이웃사람","범죄도시"],
        "애니메이션":["신데렐라","겨울왕국","하울이 움직이는 성","코난","라따뚜이"]}

while True:
 print("🎬원하는 영화 장르를 입력하세요.🎬")
 for genre in recommendationse:
    print(f" {genre}")

 choice_genre =input("장르 입력 :")

 if choice_genre in recommendationse :
    print(f"[{choice_genre}]추천작품 :")
    for title  in recommendationse[choice_genre]:
        print(f"추천 작품은 :{title}입니다.")
 else :
    print("존재하지 않는 장르 입니다.")    
 print("종료를 원하시면 0 번 계속 추천 받고 싶다면 1 번을 눌러주세요.")
 choice = input()
 if choice =="0" :
    print("😊종료하겠습니다.😊")
    break
 elif choice =="1":
    print ("😊추천페이지로 돌아가기😊")
