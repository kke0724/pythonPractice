print('-'*30)

print("cm   mm    m    inch")

print('-'* 30)

for cm in range(1, 51):
    mm = cm * 10
    m = cm * 0.01
    inch = cm * 0.3937
    print('%3d %6.0f %8.2f  %8.2f' % (cm, mm, m, inch))

print('-'*30)