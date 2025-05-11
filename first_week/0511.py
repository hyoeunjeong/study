#01. Id 와 비밀번호를 입력받고,다음과 같은 조건이면 로그인 성공이라고 출력하시오
## - Id가 "admin" 또는 "user"
## 비밀 번호는 "1234"
#print("ID:")
#user_id = input()
#print("password:")
#password = input()

#if (user_id == "admin" or user_id == "user") and password == "1234":
#    print("로그인에 성공하였습니다.")
#elif (user_id != "admin" and user_id != "user") and password == "1234":
#    print("ID를 다시 입력하시오.")
#elif (user_id == "admin" or user_id == "user") and password != "1234":
#    print("비밀번호를 다시 입력하시오.")
#else:
#    print("ID와 비밀번호를 다시 입력하세요.")

##02. 사용자에게 비밀번호를 입력받아,다음조건을 모두 만족하면 "유효한 비밀번호"를 출력하시오
##-8자 이상
##"!"또는 "#"기호가 포함되어있음
#print("비밀번호를 입력하시오 ")
#password = input()
#if len(password) >= 8 and ("!" in password  or "#" in password) :
#        print("유효한 비밀번호 입니다.")
#else: 
#    print("유효하지 않는 비밀번호 입니다.")


##3. 별 피라미트 출력
#사용자에게 정수 N을 입력 받아 아래와 같은 별 피람미드 출력하시오
##(예 : N=3)
#print("정수를 입력하시오 :")
#N =  int(input())
#for i in range(1,N+1) :  #1부터 N+1 까지 반복
#    space =' '* (N-i)    ## 빈칸  공백 개수 = N - 줄번호
#    stars ='*'*(2 *i -1) ## 별 별 개수 = 2 * 줄번호 - 1
#    print(space+stars)
##4. 딕션너리 값을 기준으로 내림차순으로 정렬한 리스트를 출력하시오.

test_score ={"kim":67,"yang":86,"jeong":57,"lee":90,"kang":100}
sorted_list =sorted(test_score.items(),reverse=True)   ##True --내림차수
print(sorted_list)

##5.구구단 2단부터 9단까지 for문으로 작성해서 출력하시오

#for i in range(2,9):
#    for j in range(1,9):
#        print(f"{i}단: {i}*{j} ={i*j}")


