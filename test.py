

n = input("Nhập vào 1 dãy số, cách nhau bởi dấu ' ':")
n+=" "
x = ""
lis = []
for i in n:
    if i !=" ":
        x+=i
    else:
        lis.append(x)
        x=""

lis.reverse()
for i in lis:
    print(i)

    
    