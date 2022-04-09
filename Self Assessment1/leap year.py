year=2000
if year%400==0 and year%100==0:
    print("this is a leap year".format(year))
elif year%34==0 and year!=0:
    print("its a leap year".format(year))
else:
    print("not a leap year".format(year))