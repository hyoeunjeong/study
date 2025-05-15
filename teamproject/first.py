'''
1-1. signup() – 회원가입 기능
힌트:
input() 을 사용하여 사용자가 ID와 비밀번호를 입력받습니다.
이미 존재하는 ID는 users 딕셔너리에서 확인하여 중복을 방지합니다.
users[username] = password 로 딕셔너리에 사용자 정보를 저장합니다.
1-2. login() – 로그인 기능
힌트:
로그인 시 ID와 비밀번호를 확인하고, 일치하면 current_user 에 로그인된 사용자를 저장
합니다.
로그인에 실패하면 아이디나 비밀번호 오류 메시지를 출력합니다.'''
'''
🧩 signup() 메서드 힌트
input()으로 아이디, 비밀번호 입력 받기

self.users에 아이디가 이미 있는지 확인

없으면 self.users[아이디] = 비밀번호 저장
'''

## 로그인 하기
class systeam:
    def __init__(self):
        self.users ={}
        self.current_user = None
         

   
## 회원가입하기
    def signup(self):
     username =input("아이디를 입력하시오.")
     if username in self.users:
        print("이미 존재하는 아이디 입니다. 다시 입력해주세요.")
        return 
     password =input("비밀번호를 입력하시오")
     self.users[username] =password
     print(f"{username}님🎉회원가입이 완료 되었습니다.🎉")

    def login(self):
     username = input("아이디를 입력하세요: ")
     password = input("비밀번호를 입력하세요: ")

     if username in self.users and self.users[username] == password:
            self.current_user = username
            print(f"{username}님, 로그인 성공!")
     else:
            print("아이디 또는 비밀번호가 올바르지 않습니다.")
##로그인하기 
''' 
login() 메서드 힌트
input()으로 아이디, 비밀번호 입력 받기

아이디가 존재하고, 비밀번호도 일치하면 self.current_user = 아이디

그렇지 않으면 오류 메시지 출력
'''
