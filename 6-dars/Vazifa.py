# '1'
# k = int(input("k="))
# n = int(input("n="))
# for i in range(n):
#     print(k)
# '1'
# b = int(input("b="))
# a = int(input("a="))
# for i in range(b,a+1):
#     print(i)
# print(a-b)
# '3'
# b = int(input("b="))
# a = int(input("a="))
# for i in range(b,a-1,-1):
#     print(i)
# print(b-a)
#'7'
# b = int(input("b="))
# a = int(input("a="))
# sum=0
# for i in range(a,b+1):
#     sum=sum+i
# print(sum)
# '8'
# b = int(input("b="))
# a = int(input("a="))
# s=1
# for i in range(a,b+1):
#     s=s*i
# print(s)
#'9'
# a = int(input("a="))
# b = int(input("b="))
# s=0
# for i in range(a,b+1):
#     s=s+i**2
# print(s)
# '10'
# n = int(input("n="))
# s=0
# for i in range(1,n+1):
#     s=s+1/i
# print(s)
# '11'
# n = int(input("n="))
# s=0
# for i in range(n+1):
#     s=s+(n+i)**3
# print(s)
# '14'
# n = int(input("n="))
# s=0
# for i in range(1,n+1):
#     s=s+(2*i-1)
#     print(s)
# '20'
# n = int(input("n="))
# s = 1
# l = []
# for i in range(1,n+1):
#     s=s*i
#     l.append(s)
# print(sum(l))
# '22'
# x = int(input("x="))
# n = int(input("n="))
# s = 1
# l = []
# for i in range(n+1):
#     for i in range(i+1):
#         if i==0:
#             s=1
#         else:s=s*i
#     l.append((x**n)/s)
# print(sum(l))
#
# '23'
# import math
#
# x = int(input("x="))
# n = float(input("n="))
# s=0
# for i in range(1,int(n+1)):
#     s=s+(pow(-1,i)*pow(x,2*i-1))/(math.factorial(2*i-1))
# print(s)
#
# '24'
# import math
#
# x = float(input("x="))
# n = int(input("n="))
# s=0;
# for i in range(n+1):
#     s=s+(pow(-1,i)*(pow(x,2*i)))/(2*math.factorial(i))
# print(s)
#
'27'
import math

'28'

# '29'
# a = float(input("a="))
# b = float(input("b="))
# n = int(input("n="))
# h = math.fabs(a-b)/n
# l = []
# if a > b:
#     for i in range(n):
#         c=b+i*h
#         l.append(c)
# elif a < b:
#     for i in range(n):
#         c=a+i*h
#         l.append(c)
# print(l,h)
#
# '31'
# n = int(input("n="))
# a = [2]
# for i in range(1,n+1):
#     c = 2 + 1/(a[i-1])
#     a.append(c)
# del a[0]
# print(a)
#
# '33'
# n = int(input("n="))
# a = [1,2]
# for i in range(0,n-2):
#     c = a[i] + a[i+1]
#     a.append(c)
# print(a)
#

