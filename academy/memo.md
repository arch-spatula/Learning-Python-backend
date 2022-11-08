# 개발자가 검색

개발자 검색하는 것은 괜찮지만 검색도 못하면 곤란합니다.

파이썬을 검색할 수 있을 정도로 지식을 습득합니다.

검색하는 것도 프로그래밍 스킬은 아니지만 일잘하는 스킬은 맞습니다.

```py
# hello.py
print('hello, world!')
```

# 연산

```py
a = 3        # 3을 a에 넣는다.
print(a)
b = a        # a에 들어 있는 값인 3을 b에 넣는다.
print(b)
a = 5        # a에 5라는 새로운 값을 넣는다.
print(a, b)  # 5 3
```

파이썬은 식별자에 업데이트를 간단하게 할 수 있습니다. 참조하는 방식이 자바스크립트랑 상당히 다릅니다. 자바스크립트였으면 `b`도 같이 업데이트 되었을 것입니다.

```py
# 나머지 연산자
a = 7
b = 2
a//b  # 3 (몫)
a%b   # 1 (나머지)
a**b  # 49 (거듭제곱)
```

# 자료형

```py
3  # 정수형 int
3.3  # 소수형 float
True  # 부울리안 True
False  # 부울리안 False
```

논리연산을 지원하는 방식이 자연스럽습니다.

```py
a = 4 > 2  # True
not a      # False    NOT 연산자로 참을 거짓으로, 거짓을 참으로 바꿔준다.

a and b    # False    AND 연산자로 모두 참이어야 참을 반환한다.
a or b     # True     OR 연산자로 둘 중 하나만 참이면 참이다.
```

```py
# 평균을 구해보세요
a = 24
b = 16
c = 26

def avg(Array):
    return sum(Array)//len(Array)

print(
    avg([a, b, c])
)
```

숫제풀이입니다.

# 문자열 다루기

`''`, `""` 큰따옴표 작은 따옴표 모두 문자열을 만들 수 있습니다.

자료형을 알아내는 방법은 `type()` 내장함수를 활용합니다.

```py
firstName = 'kim'

print(type(firstName))  # <class 'str'>
```

자바스크립트랑 다르게 근본이 있어서 숫자랑 문자열이랑을 더하면 막습니다.

```py
print('2' + 2)  # TypeError: can only concatenate str (not "int") to str
```

디자인이 잘 되어 있는 언어 답게 에러를 돌려줍니다.

```py
sentence = 'Python is FUN!'

sentence.upper()  # PYTHON IS FUN!
sentence.lower()  # python is fun!
```

```py
# 이메일 주소에서 도메인 'gmail'만 추출하기
myemail = 'test@gmail.com'

result = myemail.split('@') # ['test','gmail.com'] (뒤에 배울 '리스트'라는 자료형이에요 :))

print(result)
```

# 슬라이싱

`[]`에는 인덱스로 하나의 값만 찾는 것이 아닙니다. 여러 값을 찾을 수 있습니다.

```py
슬라이싱대상[시작할 인덱스 : 종료할 인덱스 + 1]
```

슬라이싱이 이렇게 생겼습니다.

```py
f="abcdefghijklmnopqrstuvwxyz"

print(f[4:15])  # efghijklmno           f[4]부터 f[15] 전까지, 총 15-4=11개!

print(f[:])  # abcdefghijklmnopqrstuvwxyz  처음부터 끝까지
```

파이썬에서 `[:]`은 복사입니다. 놀랍습니다.

또 파이썬은 인덱스로 음수도 입력할 수 있습니다. 음수면 마지막 값을 조회할 수 있습니다.

```py
f="abcdefghijklmnopqrstuvwxyz"

print(f[-1])  # z
```

# len 내장함수

```py
print(len('abc'))  # 3
```

문자열, list, tuple 등 사용할 수 있습니다.

# 리스트와 딕셔너리

리스트(`list`)와 딕셔너리(`dictionary`)는 다양한 값을 담을수 있는 자료형입니다.

리스트는 순서가 있습니다.

```py
a = [1, 2, 3, 4, 5]

a.append(99)

print(a)
```

`in` 연산으로 탐색도 가능합니다.

`sort`로 정렬도 가능합니다.

```py
a = [1, 2, 3, 4, 5]

a.append(99)
a.sort(reverse=True)

print(6 in a)
```

딕셔너리는 `key`와 `value`로 값을 저장합니다. 딕셔너리에는 순서가 없는 것처럼 취급합니다.

```py
a = {
    'name': 'Jake',
    'age' : 30,
}

print(a['name'], a['age'])  # Jake 30
```

```py
a = {
    'name': 'Jake',
    'age' : 30,
}

a['height'] = 'inf'

print('height' in a)
print('inf' in a)
```

`in` 연산은 `key`의 존재여부를 기준으로 판단합니다. `value`의 존재여부는 다르게 알아내야 합니다.

# 조건문

파이썬은 다른 언어랑 다르게 들여쓰기가 강제됩니다.

```py
age = 27
if age < 20: print("청소년입니다.")
elif age < 65: print("성인입니다.")
else: print("무료로 이용하세요!")
```

하지만 1줄일 때는 개행하지 않고 같은 줄에 작성도 가능합니다.

# 반복문

```py
fruits = ['사과', '배', '감', '귤']

for fruit in fruits:
    print(fruit)
```

반복문을 `list`에서 하나식 조회합니다.

```py
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    [name, age] = [person['name'], person['age']]
    print(name, age)
```

신기하게 구조분해 할당을 지원하고 있습니다.

```py
for idx, person in enumerate(people):
    [name, age] = [person['name'], person['age']]
    print(idx, name, age)
```

`enumerate`내장함수는 우아하게 반복문에서 순회횟수를 알아낼 수 있습니다. `range(len())`같은 방식에 의존하지 않을 수 있습니다.

연습문제

```py
num_list = [1, 2, 3, 6, 3, 2, 4, 5, 6, 2, 4]

def solution(Array):
    result = []
    for elem in Array:
        if elem % 2 == 0: result.append(elem)
    return result

print(solution(num_list))
```

# 함수

프로그래밍에서의 함수는 동일한 동작을 실행시키기 위해 사용합니다.

```py
def check_gender(pin):
    [first, second] = pin.split('-')
    if int(second[0]) % 2 == 0 : print('여성')
    else : print('남성')

my_pin = '200101-3012345'
check_gender(my_pin)
```

# 더 많은 문제 해결

여기부터 배우면 더 많은 문제를 더 효율적이게 해결할 수 있습니다.

# 튜플(tuple)과 집합(set)

튜플은 리스트랑 동이하지만 ReadOnly입니다.

```py
aTuple = (1, 2, 3)

aTuple[0] = 5  # TypeError: 'tuple' object does not support item assignment
print(aTuple)
```

역시 신뢰할 수 있는 에러메시지를 돌려줍니다.

당연히 소프트웨어가 방대해졌고 데이터 뮤테이션을 최대한 제어하기 위해 사용할 것입니다.

집합은 중복을 제외해줍니다.

```py
aSet = {1, 2, 3, 3, 3, 2, 1}

print(aSet)
```

수학적인 개념과 유사하게 집합연산을 지원합니다.

```py
a = set(['사과','감','수박','참외','딸기'])
b = set(['사과','멜론','청포도','토마토','참외'])

print(a & b)  # 교(and) 집합
print(a | b)  # 합(or)  집합
print(a - b)  # 차(not) 집합
```

중복제거와 집합연산등 정렬과 필터에 응용할 수 있습니다.

# f-string

문자열 다룰 때 자주사용합니다.

```py
f'{변수} 문자열'
```

보통은 면수를 넣지만 다른 코드들이 갖는 값들을 넣을 수 있습니다.

# 예외처리

모든 자료를 다 처리할 수 있는 것은 아닙니다.

```py
people = [
    {'name': 'bob'},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    [name, age] = [person['name'], person['age']]
    if age > 20: print(name)
```

이런 코드는 에러가 발생할 것입니다. 하지만 에러가 발생할 때 중단을 하지 않게 만들 수 있습니다.

```py
people = [
    {'name': 'bob'},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

for person in people:
    try:
        [name, age] = [person['name'], person['age']]
        if age > 20: print(name)
    except:
        print(f'{person} 자료는 에러입니다.')
```

정상실행되는 코드중 에러가 발생하는 `bob`에 오류가 있다는 것을 추적할 수 있습니다.

테스트와 버그추적에 사용하기를 권장합니다.

# 파일불러오기

```py
# main_test.py
from main_func import asdf

asdf()
```

`from 모듈이름 import 가져올대상`이런 문법으로 파일 분리를 할 수 있습니다.

# 한줄 문법설탕

파이썬에서도 놀랍게 삼항연산자를 지원합니다.

```py
"짝수" if num % 2 == 0 else '홀수'
```

if문이 참이면 `짝수` 거짓이면 `홀수`가 됩니다.

```py
a_list  = [1, 3, 2, 5, 1, 2]

b_list = [a*2 for a in a_list]

print(b_list)
```

for문 앞에는 각원소입니다. 각원소에 2를 곱하고 저장한 것입니다. 파이썬은 FP를 지원하지 않습니다.

# map, filter, lambda

```py
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

def checkAge(person:dict):
    return '성인' if person['age'] > 20 else '아동'

print(list(map(checkAge, people)))
```

`map`은 함수에 자료를 하나씩 넣습니다.

람다는 익명함수 키워드입니다. 코드를 더욱더 우아하게 만들어줍니다.

```py
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

print(list(map(lambda person: ('성인' if person['age'] > 20 else '아동'), people)))
```

한번만 사용할 함수에 적합합니다. 보통함수를 인자로 받는 함수에 사용합니다.

```py
lambda 매개변수: 함수몸이자 반환값
```

순수하게 람다함수를 정의한 문법입니다.

```py
print((lambda x, y : x + y )(2, 3))  # 5 람다를 홀로 쓸 때 문법
```

람다함수를 정의하고 사용한 문법입니다.

함수를 콜백함수처럼 넘겨서 사용할 수 있습니다.

```py
from functools import reduce

print(reduce(lambda acc, crr: acc + crr, list(range(1, 11))))  # 55
```

람다함수를 자바스크립트의 콜백함수랑 유사하게 사용했습니다.

람다함수의 매개변수는 관례적으로 `x`라고 작성합니다.

```py
people = [
    {'name': 'bob', 'age': 20},
    {'name': 'carry', 'age': 38},
    {'name': 'john', 'age': 7},
    {'name': 'smith', 'age': 17},
    {'name': 'ben', 'age': 27},
    {'name': 'bobby', 'age': 57},
    {'name': 'red', 'age': 32},
    {'name': 'queen', 'age': 25}
]

results = filter(lambda x: x['age'] > 20, people)
print(list(results))
```

`filter`도 람다함수가 부울리안 값을 판별하고 참이면 남기고 거짓이면 빼는 코드를 작성할 수 있습니다.

# 함수

함수는 제어하기 쉽습니다.

```py
def fn(a=2, b=3):
    return a + 5*b

print(fn())  # 17
print(fn(b=1, a=6))  # 11
```

대입하는 순서도 변경할 수 있고 대입한 값이 없으면 자동으로 대입한 것으로 할 수 있습니다.

```py
def fn(*args):
    for arg in args:
        print(f'{arg}이다.')

print(fn('뇌절', '좋소'))  # 뇌절이다.\n 좋소이다.
```

```py
def fn(**kwargs):
    print(kwargs)

print(fn(상태='뇌절', 회사='좋소'))  # {'상태': '뇌절', '회사': '좋소'}
```

함수에 값을 대입하면 `dict`자료형이 되게 만들 수 있습니다.

이런 문법은 직접사용할 때도 있지만 라이브러리를 읽어보면서 자주 볼 수 있을 것입니다.

# 클래스

언제 사용하는지를 어떻게 사용할지보다 중요합니다.

객체지향적으로 유사하지만 각각 달라야 하는 존재들을 만들어야 할 때 사용합니다.

```py
class Monster():
    def __init__(self, hp) -> None:
        self.hp = hp
        self.alive = True

    def damage(self, attack):
        self.hp = self.hp - attack
        if self.hp < 0:
            self.alive = False

    def checkStatus(self):
        if self.alive: print('살아있습니다.')
        else: print('죽었습니다.')

m = Monster(100)
m.damage(120)

m2 = Monster(100)
m2.damage(90)

m.checkStatus()
m2.checkStatus()
```

`__init__` 객체생성시 초기화를 설정하는 함수입니다. `Monster()`에 무엇을 대입할지 설정하는 함수입니다.
