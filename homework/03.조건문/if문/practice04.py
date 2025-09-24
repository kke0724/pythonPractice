start = int(input("시작 수는?"))
end = int(input("끝 수는?"))
num = int(input("정수를 입력하세요:"))

result = "%d는 %d~%d 사이에 없다." %(num,start,end)

if  start <= num and end >= num:
    resuit = '%d는  %d~%D 사이에 있다' %(num,start,end)

    print(resuit)