# fixed_amount=300000
# withdraw=int(input("enter your amount :",))
# print("available balance :",fixed_amount-withdraw)
#
# USING IF ELSE CONDITION
fixed_amount=300000
withdraw=int(input("enter your amount :",))
if withdraw<fixed_amount:
    print("available balance :",fixed_amount-withdraw)
else:
    print("insufficient balance")
