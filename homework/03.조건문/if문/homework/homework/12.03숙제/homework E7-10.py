def cminch (x):
    result = x * 0.393701
    
    return result

def kgpound (y):
    result2 = y * 2.204623

    return result2

print('-선택옵션')
print('1. 길이환산 (센치미터 --> 인치)')
print('2. 무게환산 (킬로그램 --> 파운드)')

math = input('원하는 환산 단위를 선택하세요.(1/2): ')
 
if math == '1':
    cm = int(input('센티미터 단위의 길이를 입력하세요: '))
    inch = cminch(cm)
    print('%d 센티미터 --> %.2f 인치' % (cm,inch))

else:
    kg = int(input('킬로그램 단위의 무게를 입력하세요: '))
    pound = kgpound(kg)
    print('%d 킬로그램 --> %2.1f 파운드' % (kg,pound))