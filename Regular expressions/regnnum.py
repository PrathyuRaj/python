import re
f1=open('regnum','r')
f2=open('pythonreg.text','w')
x='[L][U][M]\d{2}[P]d[Y]\d{2}'
for i in f1:
    reg=i.rstrip("\n")
    match=re.fullmatch(x,reg)
    if match is not None:
        f2.write(reg)
        f2.write("\n")