# d={"name":"anu","place":"kochi","age":23}
# # del d["place"]
# # d.clear()
# # del d
# # print(d)
#
#
# # split method
# # only in string(string method)
# # , have to be used after split commad inside " "if , is used or space has to be used
# # output type=list
#
# s="hello,hi,hello"
# b=s.split(",")
# print(b)

#
#
#
#
# count={"hello":1}

s=input("enter your string")
a=s.split(" ")
wordcount={}
# print(a)
for i in a:
    if i not in wordcount:
        wordcount.update({i:1})
    else:
        value=wordcount[i]
        value+=1
        wordcount.update({i:value})
print(wordcount)
