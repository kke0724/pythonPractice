spend = int(input("구매금액은?"))

if spend >= ("1~5"):
    rate = 5.0
elif spend >= ("6~30"):
    rate = 7.5
elif spend >= ("30~"):
    rate = 10.0 
else :
    rate = 0