a = int(input("변환할 킬로그램(kg)은?"))

ponud = a*2.204623
ounce = a*35.273962

print ("-"*30)
print ('킬로그램',    '파운드',     '온스')
print ("-"*30)
print ("%.1f" % a,            "%.1f" % ponud,       "%.1f" % ounce)
print ("-"*30)