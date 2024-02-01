'''STRING VA UNICODE
STRING (matn) —Pythondagi eng mashxur ma'lumot turlaridan biri.
Avvalgi darsda ko'rganimizdek, o'zgaruvchiga matn yuklash uchun matn
qo'shtirnoq (" ") yoki birtirnoq (' ') ichida yozilishi kerak.'''

'''STRING USTIDA AMALLAR
Matnlarni qo'shish operatori (+)
Matnlarni qo'shish uchun + operatoridan foydalanmiz:'''

# ism = 'Ahmad'
# print("Mening ismim" + ism)
#
# ism = 'Ahad '
# familiya = 'Qayum'
# print(ism + ' ' + familiya)

# ism = 'Muqaddas'
# familiya = 'Komilova'
# umu_iy = ism + ' ' + familiya
# print(umu_iy)
#
'''Yuqoridagi kodda ism va familiya orasiga bo'shliq belgisini qo'shmaganimiz
uchun ikki matn qo'shilib yozildi. Buni to'g'rilash uchun, 3-qatorni quyidagicha yozamiz:'''

# ism = 'Ahad'
# familiya = 'Qayum'
# print(ism + ' ' + familiya) # ikki o'zgaruvchi orasiga bo'sh joy qo'shamiz

'''f-string
Ikki (va undan ko'p) matn ko'rinishidagi o'zgaruvchilarni birlashtirish uchun
 f-string usulidan  f"{matn1} {matn2}" ham foydalansak bo'ladi:'''

# ism = "Ahad"
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif)
#
# ism = 'Xusanboy'
# familiya = 'Miraxmedov'
# ochest = 'Usmonjon o\'gli'
# umuiy_mal = f"Mening ismim {ism} mening familiyam {familiya} ochestva {ochest} "
# print(umuiy_mal)


# '''Bu usul yordamida uzun matnlarni ham yasash mumkin:'''
#
# ism = "James"
# familiya = 'Bond'
# print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")
#
'''Maxsus belgilar
Matnga bo'shliq qo'shish uchun \t belgisidan, yangi qatordan
boshlash uchun \n belgisidan foydalanamiz:'''

# print('Hello World!')
# print('Hello \tWorld!')
# print('Hello \nWorld!')


'''STRING METODLARI
Pythonda string ustida amalga oshirish mumkin bo'lgan tayyor amallar to'plami mavjud. Bunday amallar to'plami metodlar deb ataladi.
Metodlarni qo'llash uchun metod nomi matndan so'ng .metod_nomi() ko'rinishida yoziladi. Keling shunday metodlarning ba'zilari bilan tanishaylik.
upper() va lower() metodlari
upper() metodi matndagi har bir harfni katta harfga o'zgartiradi. '''

# ism = 'ahad'
# familiya = 'qayum'
# ism_sharif = f" mening ismim {ism} mening familiyam {familiya}"
# print(ism_sharif.upper())

'''lower() metodi esa aksincha, har bir harfni kichik harfga o'zgartiradi.'''
#
# ism = 'Ahad'
# familiya = 'Qayum'
# ism_sharif = f"{ism} {familiya}"
# print(ism_sharif.lower())

# ism = 'Sardor'
# familiya = 'Maxudov'
# ism_sharif = f"Mening ismim {ism} MeNing faMILIYAM {familiya}"
#
# print(ism_sharif.lower())

'''title() va capitalize() metodlari
title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.'''

# ism_sharif = 'james bond'
# print(ism_sharif.title())

'''capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.'''

# ism_sharif = 'james bond'
# print(ism_sharif.capitalize())

'''strip(), rstrip() va lstrip() metodlari
Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
lstrip() — matn boshidagi bo'shliqni,
rstrip() – matn oxiridagi bo'shliqni,
strip() — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi'''
#
# meva = "     olma     "
# print("Men " + meva.lstrip() + " yaxshi ko'raman")
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men " + meva.strip() + " yaxshi ko'raman")
# print("Men " + meva + " yaxshi ko'raman")

#
# '''INPUT —FOYDALANUVCHI BILAN MULOQOT
# Shu paytgacha biz o'zgaruvchilarning qiymatini
# dasturning ichida berayotgan edik.
#  Keling endi qiymatni o'zimiz emas, balki dastur
#  foydalanuvchilariga kiritish imkonini beramiz.
# Buning uchun input() funktsyasidan foydalanamiz. '''

# ism = input("Ismingiz nima")
# print("Assalom alaykum, " + ism)
#
# ism = input("Ismingiz nima?\n>>>") # Foydalanuvchi ismini yangi qatordan kiritadi
# print("Assalom alaykum, " + ism.title())


