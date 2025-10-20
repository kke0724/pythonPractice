a = int(input("시작 수를 입력해주세요 :"))
b = int(input("끝 수를 입력해주세요 :"))

c = a

while c <= b:
    d = True
    for i in range(2, c):
        if c % i == 0:
            d = False
        
    if d:
        print(c, end=" ")

    c = c + 1