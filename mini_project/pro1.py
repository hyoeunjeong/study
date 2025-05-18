
def __init__(self):
 self.users = {}  # 사용자 정보 저장용 딕셔너리

def signup(self,username):  # 회원가입 함수
    while True:
        username = input("아이디를 입력하세요: ")
        if username in self.users:
            print("❗ 이미 존재하는 아이디입니다.")
        else:
            break
    password = input("비밀번호를 입력하세요: ")
    self.users[username] = password
    print(f"🎉 {username}님, 회원가입이 완료되었습니다!")

def login(self,username,password):  # 로그인 함수
    username = input("아이디를 입력하세요: ")
    password = input("비밀번호를 입력하세요: ")
    if username in self.users and self.users[username] == password:
        print(f"✅ {username}님, 로그인 성공!✅")
    else:
        print("❌ 아이디 또는 비밀번호가 올바르지 않습니다.❌")




