print("아라바이트 급여 계산 프로그램")
print("시급")
print("-주간근무:9500원")
print("-야간근무 : 주간 시급*1.5")
print()

hour_pay = 9500

a = int(input ("1(주간근무) 또는 2(야간근무)을 입력해주세요:"))
work_time = int(input("근무시간을 입력해주세요:"))

if ("주간근무"):
 day_night = "주간"
 pay = hour_pay*work_time

else:
  day_night = "야간"
  pay = hour_pay* work_time * 1.5

print('%d시간동안 일한 %s 급여는 %d원 입니다.' %(work_time,day_night,pay))
