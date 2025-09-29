char = input("영문 대문자 또는 소문자를 입력하세요:")
char2 = char.upper()

if char2 == 'A' or 'I' or 'E' or 'O' or 'U':

 print("%s-> 모음" % char)

else:
 print("%s->자음" % char)