def str(string):
    result = " "
    math = len(string)
    while math > 0:
        result = result + string[math - 1]
        math = math - 1

    return result

string = input('문자열을 입력하세요: ')
print(str(string))