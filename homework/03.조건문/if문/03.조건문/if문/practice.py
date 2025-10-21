a = int(input('현재 년은?'))
b= int(input('현재 월은?'))
c=int(input('현재 일은?'))

a2= int(input('출생 년은?'))
b2=int(input('출생 월은?'))
c2=int(input('출생 일은?'))

if b2 < b:
    age = a - a2

elif b2 == b:
 if c2-c:
    age = a-a2
 else:
    age= a-a2 -1

else:
   age = a - a2 -1



print(f'오늘 날짜:{a,b,c}')
print(f'생년월일: {a2,b2,c2}')
print(f'나이: {age}')