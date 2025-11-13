dic = {}

while True:
    key = input('단어(삭제:0,  종료:1)')
    if key == '1':
        break
    elif key == '0':
        a = input('삭제할 단어:')
        dic.pop(a)
    else:
        value = input('뜻 입력')
        dic[key] = value
    print('헌재 사전:', dic)