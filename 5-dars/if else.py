"""if OPERATORI
if so'zi ingliz tilidan "agar" deb tarjima qilinadi va deyarli barcha dasturlash tillarida
shartlarni yozish uchun foydalaniladi.
Keling quyidagi misolni ko'ramiz. Bizda avtolar ro'yxati bor:"""

# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ...
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilann yoz.

'''1-qatorda biz for tsiklini boshladik: avto ichidagi har bir avto uchun.
2-qatorda shart yozdik: agar avto bmw ga teng bo'lsa (bu yerda == belgisi tenglikni tekshirish 
belgisi hisoblanadi va "avto bmw ga tengmi?" deb o'qiladi).
3-qator yuqoridagi shartning badani hisoblanadi va faqatgina shart bajarilgandagina ishga 
tushadi va avto nomini hamma harflarini katta bilan yozadi (.upper() metodi).
4-qatorda yana bir yangi operator, else bilan tanishamiz. "Else" ingliz tilidan "aks holda"
deb tarjima qilinadi va if sharti bajarilmaganda else qismi ichidagi kod bajariladi.
5-qator esa else (aks holda, ya'ni 2- qatordagi shart bajarilmaganda) ishga tushadi va 
avto nomining faqat birinchi harfini katta bilan yozadi (.title() metodi)
Diqqat! Shart "badani" shartdan biroz o'ngga surib yoziladi (huddi for tsikli kabi). 
if/else dan keyin kelgan va o'ngga surib yozilgan har bir qator if/else shartining badani hisoblanadi.
Yuoqridagi kodni bajaramiz, va natijani ko'ramiz:'''
# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar: # avtolar ichidadi har bir avto uchun ...
#     if avto == 'bmw':  # ... agar avto bmw ga teng bo'lsa ...
#         print(avto.upper()) # avto nomini hamma harflarini katta bilan yoz.
#     else: # aks holda ...
#         print(avto.title()) # avto nomini faqat birinchi harfini katta bilan yoz.




'''Demak yuqoridagi kodning 2-qatorida ism ichidagi qiymat 'ali' ga teng bo'lmasa "Uzr, 
{ism} biz Alini kutyapmiz" degan xabarni chiqar dedik. Aks holda (else), "Salom, Ali" 
degan xabar chiqadi.
Shartlarda else qismi bo'lishi majburiy emas. Bunga keyingi bo'limlarda tushunarliroq 
misollar ko'ramiz.

SONLARNI SOLISHTIRISH
Sonlarni solishtirishda yuqoridagi teng (==) va teng emas (!=) shartlariga qo'shimcha 
ravishda quyidagi mantiqiy shartlar ham qo'shiladi:
Kichik: a<b
Kichik yoki teng: a<=b
Katta: a>b
Katta yoki teng: a>=b'''

# javob = float(input("12x6 nechiga teng>>>"))
# if javob != 72:
#     print("Javob xato!")
#
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh >= 18: # yosh 18 dan katta yoki teng bo'lsa
#     print('Xush kelibsiz! mehmon keling oshga marhamat')
# else: # ask holda
#     print('Kirish mumkin emas! siz hali yoshbolasiz bu sayt 18 yoshdan yuqorilar uchun')

# login = int(input("Yangi login tanlang:"))
# if login <= 99999:
#     print("Login 5 raqamdan kam bolmasligi kerak")

# '''Sonlarni solishtirishda arifmetik ifodalar ham yozishimiz mumkin:'''
# yil = int(input("Tug'ilgan yilingizni kiriting:"))
# if 2023-yil < 18: # foydalanuvchining yoshini hisoblaymiz
#     print(f"Yoshingiz {2023-yil} da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Xush kelibsiz!")
'''
BIR QATOR if/else
Qisqa kodlar uchun shart va uning badanini 1 qatorga jamlab yozishimiz ham mumkin:'''
# yosh = int(input("Yoshingiz nechida?>>>"))
# if yosh > 65:
#     print("Siz COVID-19 risk guruhida ekansiz")


# x, y = 25, 50 # x=25 va y=50
# print("x>y") if x>y else print("x<y")
