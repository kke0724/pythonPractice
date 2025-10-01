a  =  input("아이디는?")

if a == 'admin':
    print('콘탠츠 이용이 가능합니다!')

else:
    level = int(input("회원레벨은?(1~9)"))
    if level > '0' and level < '4':
     print('콘탠츠 이용이 가능합니다')
    else:
       print('콘탠츠 이용이 불가합니다')