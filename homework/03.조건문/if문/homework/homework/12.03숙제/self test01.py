def sum_int(start,end):
    total = 0
    for i in range(start,end + 1):
        total = total + i
    print('%d ~ %d 정수의 합계: %d' % (start, end ,total))

sum_int(1005,21452847662)