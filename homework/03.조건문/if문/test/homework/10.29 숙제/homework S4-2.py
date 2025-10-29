i = int(input('성적을 입력하시오:'))
while i != 'q':
    if i>= 90:
        print('등급:수')
    elif i>= 80:
        print('등급:우')
    elif i>= 70:
        print('등급:미')
    elif i>= 60:
        print('등급:양')
    else:
        print('등급:가')

    z = int(input('계속하시겠습니까?(중단:q,계속:y)'))
    if z == 'q':
            break

i = int(input('성적을 입력하시오:'))
