def reverse_sentense(s):
    words = s.split(' ')
    result = ''
    for word in words:
        result = word +''+result

    return result

sentense = 'Nice to meet you'
print(reverse_sentense(sentense))