set1={1,2,3,4,5,6,7}
set2={4,5,6,7,8,9,10}
common=set()
for i in set1:
    if i in set2:
        common.add(i)
print(common)

