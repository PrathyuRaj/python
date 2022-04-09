#to amke aword count dictionary rom textfile

f=open('wordcount.txt','r')
d=dict()
count=0
for i in f:
    i=i.strip()
    i=i.lower()
    words=i.split(" ")
    for word in words:
        if word in d:
            d[word]=d[word]+1
        else:
            d[word]=1
for key in list(d.keys()):
    print(key,":",d[key])


