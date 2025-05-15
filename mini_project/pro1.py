users = {}  # 사용자 정보 저장용 딕셔너리

def signup():  # 회원가입 함수
    while True:
        username = input("아이디를 입력하세요: ")
        if username in users:
            print("❗ 이미 존재하는 아이디입니다.")
        else:
            break
    password = input("비밀번호를 입력하세요: ")
    users[username] = password
    print(f"🎉 {username}님, 회원가입이 완료되었습니다!")

def login():  # 로그인 함수
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    if username in users and users[username] == password:
        print(f"✅ {username}님, 로그인 성공!✅")
    else:
        print("❌ 아이디 또는 비밀번호가 올바르지 않습니다.❌")




### 예시메뉴
while True:
    menu = input("\n1: 회원가입 | 2: 로그인 | 3: 종료 ▶ ")
    if menu == "1":
        signup()
    elif menu == "2":
        login()
    elif menu == "3":
        print("👋 프로그램을 종료합니다.")
        break
    else:
        print("❗ 올바른 메뉴 번호를 입력해주세요.")
    