# '5'
# a = float(input("a="))
# b = float(input("b="))
# c = float(input("c="))
# if (a+b+c)<1:
#     if a>c and b>c:
#         c=(a+b)/2
#     if b>a and c>a:
#         a=(c+b)/2
#     if a>b and c>b:
#         b=(a+c)/2
# elif a>b:
#     b=(a+c)/2
# elif b>a:
#     a=float((b+c)/2)
# print("a=",a,"b=",b,"c=",c)

# '8'
# n = int(input("n="))
# k = n*n
# list = []
# s = []
# for i in range(k):
#     a = float(input(f"{i+1}-elementni kiriting:"))
#     list.append(a)
# for m in range(n):
#     for i in range(1,n):
#         a = list[i*n + m]
#         s.append(a)
# print(sum(s))

#
# '16'
# import math
#
# x1 = float(input("x1="))
# y1 = float(input("y1="))
# x2 = float(input("x2="))
# y2 = float(input("y2="))
# x3 = float(input("x3="))
# y3 = float(input("y3="))
# a,b,c = 0,0,0
# ab=math.sqrt(pow((x1-x2),2)+pow((y1-y2),2))
# bc=math.sqrt(pow((x2-x3),2)+pow((y2-y3),2))
# ac=math.sqrt(pow((x1-x3),2)+pow((y1-y3),2))
# if ab+bc>ac:
#     a=1
# if ab+ac>bc:
#     b=1
# if ac+bc>ab:
#     c=1
# if (a+b+c)==3:
#     print("Berilgan nuqtalardan uchburchak yasash mumkin")
# else:print("Berilgan nuqtalardan uchburchak yasab bo'lmaydi")

# '25'
# n = int(input("n="))
# k = 1
# for i in range(1,n+1):
#     k=k*(1+1/(pow(-1,i)*(2*i+1)))
# print("Ko'paytma:",k)