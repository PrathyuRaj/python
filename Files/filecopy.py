f1=open('data.text','r')
f2=open('datacopy.text','a')
for i in f1:
    f2.write(i)