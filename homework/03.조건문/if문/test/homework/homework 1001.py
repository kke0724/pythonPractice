a = int(input("첫 번째 시간의 시를 입력하세요:"))
b = int(input("첫 번째 시간의 분을 입력하세요:"))

a2 = int(input("두 번째 시간의 시를 입력하세요:"))
b2 = int(input("두 번째 시간의 분을 입력하세요:"))

if a<a2:
    A=a
    B=b
    A2=a2
    B2=B

elif a==a2:
    if b<=b2:
        A = a
        B = b 
        A2 = a2
        B2 = b2
    else:
        A = a2
        B = b2
        A2 = a 
        B2 = b 

else:
    A = a2
    B = b2
    A2 = a 
    B2 = b 

print()
print("빠른시간: %d:%d" % (A,B))
print("늦은시간: %d:%d" % (A2,B2))