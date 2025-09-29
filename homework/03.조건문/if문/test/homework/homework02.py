a = int(input("수를 입력하세요:"))
              
if a>=0 and a<=9:
    print("%d는 한자리 숫자이다." % a)

elif a>=10 and a<=99:
    print("%d는 두자리 숫자이다." % a)

elif a>=100 and a<=999:
    print("%d는 세자리 숫자이다." %a)

else:
    print("오류! %d는 범위 이외의 숫자이다." %a)