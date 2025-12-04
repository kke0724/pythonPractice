print('-선택옵션')
print('1.더하기')
print('2.빼기')
print('3.곱하기')
print('4.나누기')

math = int(input('원하는 연산을 선택하세요(1/2/3/4): '))
math1  = int(input('첫 번째 숫자를 입력하세요: '))
math2 = int(input('두 번째 숫자를 입력하세요: '))

if math == 1:
    num = math1 + math2
    print('%d + %d = %d' % (math1, math2, num))

elif math == 2:
    num2 = math1 - math2
    print('%d - %d = %d' % (math1, math2, num2))

elif math == 3:
    num3 = math1 * math2
    print('%d x %d = %d' % (math1, math2, num3))

else:
    num4 = math1 / math2
    print('%d ÷ %d = %d' % (math1, math2, num4))