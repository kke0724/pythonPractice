def sum_int(start,end):
    total = 0
    for i in range(start,end):
        total = i
    print('%d ~ %d 정수 합계: %d' % (start,end,total))

sum_int(20,50)
sum_int(600,800)