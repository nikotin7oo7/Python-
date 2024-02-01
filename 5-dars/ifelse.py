'''if-elif-else KETMA-KETLIGI
Dastur davomida bir nechta shartni tekshirish talab qilinishi mumkin.
Bunday holatda biz if-elif-else ketma-ketligidan foydalanamiz. elif - else
va if so'zalrining jamlanmasi bo'lib, "aks holda, agar" deb tarjima qilinadi.
Bunday if bilan boshlangan ketma-ketlik bir nechta elif lardan iborat bo'lishi mumkin.
Python avval if shartini tekshiradi, shart bajarilmasa elif ga o'tadi,
birinchi elif sharti bajarilmasa keyingi elif ga o'tadi va hokazo davom etaveradi.
 Diqqat!if-elif-else ketma-ketlikda biror shart bajarilishi bilan, Python qolgan
 shartlarni tekshirmaydi.'''

'''Keling bir misol ko'ramiz. Hayvonot bo'giga kirish quyidagicha belgilangan:
4 yoshdan kichik bolalarga kirish bepul
4 yoshdan 12 yoshgacha kirish 5000 so'm
12 yoshdan kattalarga 10000 so'm
Foydalanuvchidan yoshini so'rab, hayvonot bog'iga kirish chiptasi narhini
chiqaruvchi dastur yozamiz.'''

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     print('Sizga kirish bepul.')
# elif yosh <= 12 and yosh > 4:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

'''Yuqoridagi kod avval foydalanuvchi yoshini so'raydi.
2-qatorda yosh 4 dan kichik ekanligini tekshiradi.
Agar bu shart bajarilsa shartlarni tekshirish shu yerdayoq to'xtaydi
va keyingi shartlar tashlab o'tib ketiladi.'''

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# else:
#     price = 10000
#
# print(f"Sizga kirish {price} so'm")

'''if -elif - else zanjirida bit nechta elif lar 
bo'lishi mumkin. Misol uchun, hayvonot bog'i qariyalar uchun 
chegirma e'lon qilsa, kodimizni quyidagicha o'zgartirishimiz mumkin:'''

# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:  # yosh bolalarga bepul
#     price = 0
# elif yosh <= 12:  # 4 dan 12 yoshgacha 5000 so'm
#     price = 5000
# elif yosh < 65:  # 12 dan katta va 65 dan kichiklarga narh 10000 so'm
#     price = 10000
# elif yosh <= 80:
#     price = 8000
# else:        # qariyalarga esa 8000 so'm
#     price = 0
# print(f"Sizga kirish {price} so'm")

'''AND, OR OPERATORLARI
Yuqorida aytganimizdek, if-elif-else zanjirida shartlarning biri bajarilishi bilan,
Python qolgan shartlarni tekshirmaydi va ularni bajarmaydi. Lekin ba'zida biz 2 
yoki undan ko'p shartlarni tekshirishni talab qilishimiz mumkin, buing uchun AND 
va OR operatorlaridan foydalanamiz.

OR OPERATORI
OR ingliz tilidan "yoki" deb tarjima qilinadi, va ikki va undan ko'p shartlardan
biri bajarilishini tekshirishda ishlatiladi. Quyidagi misolni ko'raylik, 
foydalanuvchidan hafta kunini so'raymiz va agar kun shanba yoki yakshanba 
bo'lsa, bugun dam olish kuni degan xabarni chiqaramiz, aks holda bugun ish 
kuni degan xabarni chiqaramiz:'''

# kun = input("Bugun nima kun?>>>")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

'''2-qatrodagi or operatoriga e'tibor qiling, bu operator kun.lower()=='shanba'
yoki kun.lower()=='yakshanba' shartlaridan biri bajarilsa TRUE qiymatini qaytaradi'''

'''AND OPERATORI
AND ingliz tilidan "va" deb tarjima qilinadi, va ikki va undan ko'p shartlarning 
barchasi bajarilishini tekshirishda ishlatiladi. AND operatori bilan yozilgan
shartlarning barchasi bajarilgandagina TRUE qiymati qaytadi, agar shartlardan 
biri bajarilmay qolsa ham FALSE qiymati qaytadi.'''

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("Cho'milgani ketdik!")
# elif kun.lower()=='yakshanba' and harorat < 30:
#     print("Uyda dam olamiz!")
# else:
#     print("ishga booor")

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if not(kun.lower() == 'yakshanba', harorat <= 30):
#     print("Cho'milgani ketdik!")
# else:
#     print("______")
'''3-qatordagi and operatori kun.lower()=='yakshanba' va harorat>=30 
shartlarining ikkisi ham bajarilgandagina TRUE qiymatini qaytaradi, aks holda 
qiymat FALSE bo'ladi.'''

'''BIR NECHTA SHARTLARNI KETMA-KET YOZISH
Shartlarni yozishda bir nechta and or operatorlarini aralashtirib ham yozish mumkin.'''



# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")

'''3-qatorga e'tibor bersangiz biz avval kun shanba yoki yakshanba ekanligini 
so'ngra haroratni tekshirdik. Bu shart bajarilishi uchun kun shanba yoki yakshanba
va harorat 30 dan baland bo'lishi shart.'''


# a = int(input("a="))
# b = int(input("b="))
# c = int(input("c="))
# if a > b > c or c > b > a:
#     print(b)
# elif b > a > c or c > a > b:
#     print(a)
# else:
#     print(c)


