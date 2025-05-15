

## fitter
'''
 filter() 함수란?
filter(function, iterable)

function: 각 요소에 적용될 함수 (True/False 반환)

iterable: 리스트, 튜플 등 반복 가능한 객체

filter()는 iterable의 각 요소에 대해 function을 적용하고, 그 결과가 True인 요소만 걸러냅니다.

반환값은 **필터 객체(filter object)**이므로, 일반적으로 list()로 감싸서 리스트로 변환합니

'''
#1. **짝수만 걸러내기**
#   정수 리스트에서 짝수만 걸러내세요.
#   예: `[1, 2, 3, 4, 5, 6]` → `[2, 4, 6]`

#numbers = [1, 2, 3, 4, 5, 6]
#even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
#print(even_numbers)


#2. **3의 배수만 걸러내기**
#   1부터 30까지의 숫자 중 3의 배수만 출력하세요.

#def f(x):
# return x % 3 ==0 
#Number =range(1,31)
#result = list(filter(f, Number))
#print(result)
#3. **음수만 걸러내기**
#   리스트 `[-5, 3, -1, 101, 0, -20]`에서 음수만 걸러내세요.


#def f (x):
# return x < 0

##miNumber =[-5, 3, -1, 101, 0, -20]

#result =list(filter(f,miNumber))

#print(result)

#4. **문자열 리스트에서 길이가 5 이상인 문자열만**
#   `['apple', 'hi', 'banana', 'go', 'cherry']`에서 길이가 5 이상인 단어만 출력하세요.

#def f(x):
# return len(x) >= 5
#word =['apple', 'hi', 'banana', 'go', 'cherry']
#result = list(filter(f,word))
#print(result)
#5. **공백 없는 문자열만 걸러내기**
#   `['hello', 'good bye', 'hi', 'see you', 'yes']`에서 공백이 없는 문자열만 걸러내세요.

def f(x):
 return ' ' not in  x
text =['hello', 'good bye', 'hi', 'see you', 'yes']
result = list(filter(f,text))
print(result)

#6. **대문자로 시작하는 단어만 걸러내기**
#   `['Apple', 'banana', 'Cherry', 'date', 'Elderberry']`에서 대문자로 시작하는 단어만 출력하세요.  ##isupper () --대문자/islower()--.소문자 

def f(x):
 return x[0].isupper()
words =['Apple', 'banana', 'Cherry', 'date', 'Elderberry']
result = list(filter(f,words))
print(result)
#7. **리스트에서 숫자만 추출하기**  isinstance() 주어진 객체가 해당 객체가 맞는지 확인하는것것
#   `['a', 1, 'b', 2, 3.5, 'hello', 10]`에서 숫자(int 또는 float)만 걸러내세요.
#isinstance(object, classinfo) 
#object: 검사할 객체 (변수, 값 등)

#classinfo: 비교할 클래스나 데이터 타입 (하나의 클래스일 수도 있고, 클래스 튜플일 수도 있음)
def f(x):
 return isinstance(x,(int,float))
li =['a', 1, 'b', 2, 3.5, 'hello', 10]
result =list(filter(f,li))
print(result)

#8. **0이 아닌 숫자만 걸러내기**
#   `[0, 1, 0.0, 3, 4, 0, -5]`에서 0 또는 0.0이 아닌 값만 걸러내세요.

def f(x):
 return x != 0
number = [0, 1, 0.0, 3, 4, 0, -5] 
result = list(filter(f,number))
print(result)

#9. **소수(1과 자기 자신만으로 나누어지는 수)만 걸러내기**
 #  2부터 50까지 숫자 중 소수만 걸러내세요. (힌트: 소수 판별 함수를 정의한 후 사용)



#10. **True 값만 걸러내기**
#리스트 `[True, False, 0, 1, '', 'hello', [], [1, 2], None]`에서 bool 값이 `True`로 평가되는 요소만 걸러내세요.

