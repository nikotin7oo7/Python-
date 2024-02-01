'1'
l=1025
m=1025//100
print("1.Metr= ",m)

'2'
m=5000
l=5000//1000
print("2.Kilogram: ",m)

'3'
b=2048
l=2048//1024
print("3.Kilobayt:",l)

'4'
a=24
b=3
l=a//b
print("4.n= ",l)

'5'
a=25
b=3
l=a//b*b
print("5.n= ",l)

'6'
a=65
b=a//10
c=a%10
print("6.Butun qismi:",b,"  Kasr qismi:",c)

'7'
a=76
b=(a//10)+(a%10)
c=(a//10)*(a%10)
print("7.Yig'indisi:",b," Ko'paytmasi:",c)

'8'
a=76
l=a//10+10*(a%10)
print("8.Raqamlari almashgandan so'ng: ",l)

'9'
a=324
l=a//100
print("9.Birinchi raqami:",l)

'10'
a=324
b=324%10
c=324//10%10
print("10.Oxirgi raqami:",b,"Ikkinchi raqami:",c)

'11'
a=324
l=a//10+a%10+a%100//10
print("11.Yig'indisi:",l)

'12'
a=324
l=a%10*100+a%100//10*10+a//100
print("12.Teskari son:",l)

'13'
a=324
l=a%100*10+a//100
print("13.Keyingi son:",l)

'14'
a=324
l=a%10*100+a//10
print("14.Keyingi son:",l)

'15'
a=324
l=a//100*10+a%100//10*100+a%10
print("15.Keyingi son:",l)

'16'
a=324
l=a//100*100+a%10*10+a%100//10
print("16.Keyingi son:",l)

'17'
a=1234
l=a//100%10
print("17.Yuzliklar xonasidagi son:",l)

'18'
a=1234
l=a%10000//1000
print("18.Minglar xonasidagi son:",l)

'19'
n=300
l=n//60
print("19.",l," minut o'tdi")

'20'
a=7200
l=7200//3600
print("20.",l," soat o'tdi")

'21'
a=306
l=a-a//60*60
print("21.Sekund:",l)

'22'
a=3636
l=a-a//3600*3600
print("22.Sekund:",l)

'23'
a=7230
l=a%3600//60
print("23.Minut:",l)

'24'
a=100
l=a%7
print("24.Kun:",l)

'25'
a=100
l=(a-4)%7
print("25.Kun:",l)

'26'
a=100
l=(a+1)%7
print("26.Kun:",l)

'27'
a=100
l=(a+5)%7
print("27.Kun:",l)


'28'
n=3
a=100
print("28.-----")


'29'
a=5
b=10
c=2
l=a*b//(c*c)
print('29.',l," ta kvadrat")

'30'
a=1336
l=a//100+1
print("30.",l,"-asr")
