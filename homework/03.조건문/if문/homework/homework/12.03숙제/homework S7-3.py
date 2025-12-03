def math(num):
    result = []
    for i in range(1, num + 1):
        num1 = i ** 2
        result.append(num1) 
    return result

n = int(input('n 값을 입력하세요: '))
sum = math(n)
print(sum)