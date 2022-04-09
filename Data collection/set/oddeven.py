s={1,2,3,4,5,7,9,10,12,14,16,18,20}
odd=set()
even=set()
for i in s:
    if i%2==0:
        even.add(i)
    else:
        odd.add(i)
print(odd,even)