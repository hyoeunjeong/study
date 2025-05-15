#1.사용자로부터 입력받은 정수 두 개를 더한 결과를 출력하세요
#print("정수 두개를 입력하시오 ")
#num =input().split()
#num1 =int(num[0])
#num2=int(num[1])
#print(f"두정수를 더한 결과는 {num1+num2}")



#2.문자열을 입력받아 거꾸로 출력하세요 ex)입력받은 문자가  'python so bad' -> 출력 결과는  'dab os nohtyp'
print("문자를 입력해 주시오")
text =input()

re_text=' '.join(word[::-1] for word in text.split())

print(f"출력결과는 {re_text}")



#3.숫자를 입력 받아 짝수면 'Even', 홀수면 'Odd'를 출력하세요
#print("숫자를 입력하시오")
#num =int(input())

#if num %2 ==0 :
#    print("Even")
#elif num %2 == 1 :
#    print("Odd")
#else:
#    print("다시 입력해주세요")


#4.[1, 2, 3, 4, 5]의 평균을 구하세요

#print("1,2,3,4,5의 평균을 구하시오")
#num=[1,2,3,4,5]
#average =sum(num)/len(num)
#print(f"평균은 {average}")



#5.두 리스트를 입력받아 교집합을 출력하세요
#print("리스트를 입력하시오")
#li1= list(map(int,input( ).split()))
#print("리스트를 입력하시오")
#li2 =list(map(int,input( ).split()))
#li3 =set(li1)
#li4 =set(li2)
#intersectio = li3&li4
#print(f"교집합{intersectio}")

#6.튜플 (1, [2, 3], 4)에서 리스트 요소 3을 100으로 바꾸세요

#tuple_1 =(1, [2, 3], 4)
#tuple_1 [1][1] =100
#print(tuple_1)
