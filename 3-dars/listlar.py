'''LIST BILAN TANISHAMIZ
Avvalgi darsimizda biz o'zgaruvchi yaratish, va uning ichida biror
qiymatni (matn yoki son) saqlashni o'rgandik. Bunda biz bitta
o'zgaruvchiga bitta qiymat berdik xolos.
Bugun o'rganadigan navbatdagi mal'umot turi List (ro'yxat) deb ataladi.
Ro'yxat o'z nomi bilan, bitta o'zgaruvchida bir nechta qiymatlarni saqlash
imkonini beradi. Bu qiymatlar List elementlari deyiladi. Ro'yxatda son, matn
yoki aralash turdagi elementlarni saqlash mumkin.
List quyidagicha yaratiladi:'''


# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5,2.4,6.23] # sonlar va matnlar aralash ro'yxat
# ismlar = ['ismoil','maruf','isroil','xusanboy'] # str turdagi ro'yxat
# print(sonlar)
# print(len(mevalar))

'''LIST ELEMENTLARI
Ro'yxatdagi har bir element tartib bilan joylashgani sababli,
 biz istalgan elementga uning tartib raqami (indeksi) bo'yicha murojat qilishimiz mumkin.'''

'''Dasturlash olamida indeks 0 dan boshlanadi! Ya'ni Listning birinchi 
elementing tartib raqami (indeksi) 0 ga, ikkinchi elementning indeksi 1 ga teng va hokazo'''

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# print("Birinchi meva: ", mevalar[0])
# print("Ikkinchi meva: ", mevalar[1])
# print("To'rtinchi meva: ", mevalar[3])

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# print("Birinchi meva: ", mevalar[0].title())
# print("Ikkinchi meva: ", mevalar[1].upper())

# ismlar = ['donyor','islombek','doston','kamola']
# l = ismlar[3].title()
# print(l)

# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])

# sum = [13400,12345,9876,12098,23454,3455,3455]
# umuiy_sum = (sum[1] + sum[4])
# print(umuiy_sum)

# son = [1,2,3,4,5,6,7]
# son1 = [2,3,4,5,56,67]
# umumiy_son = son1 + son
# print(umumiy_son)

# car_model = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_model[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz

'''ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
Dastur davomida listning tarkibi o'zgarishi, yangi elementlar qo'shilishi,
 ba'zi elementlar o'chirilishi tabiiy hol. Misol uchun "Bozorlik ro'yxati" degan 
 dasturni tasavvur qilaylik, foydalanuvchi ro'yxatga yangi mahsulotlar qo'shishi, 
 sotib olganlarini esa o'chrishi mumkin. '''

''' Elementni o'zgartirish
Ro'yxatdagi biror elementning qiymatini o'zgartirish uchun, 
o'sha elementga indeksi bo'yicha murojat qilamiz va yangi qiymat yuklaymiz'''


# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000 # 1-qiymatni 13000 ga o'zgartiramiz
# narhlar[2] = 11000 # 3-qiymatni 11000 ga o'zgartiramiz
# narhlar[3] = narhlar[3]+2000 # 4-qiymatga 2000 qo'shamiz
# print(narhlar)

'''Yangi element qo'shish
.append() metodi
Ro'yxatga yangi element qo'shishning oson usuli 
bu .append() metodi yordamida ro'yxatning oxiriga qiymat qo'shish:'''

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik","apelsin"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# mevalar.append('nok')
# print(mevalar)

# qurq_meva = ['yong\'oq','bodom','pista','yeryong\'oq']
# qurq_meva.append('olmaxon yong\'oqi')
# print(qurq_meva)

# cars = [] # bo'sh ro'yxat yaratamiz
# cars.append('Lacetti') # ro'yxatga Lacetti mashinasini qo'shamiz
# cars.append('Nexia 3') # ro'yxatga Nexia 3 mashinasini qo'shamiz
# cars.append('Cobalt')  # ro'yxatga Cobalt  mashinasini qo'shamiz
# print(cars)

# ismlar = []
# ismlar.append('xusanboy')
# ismlar.append('muslima')
# ismlar.append('lobar')
# print(ismlar)

'''.insert() metodi
Ro'yxatning istalgan joyiga yangi element qo'shish 
uchun .insert() metodidan foydalanamiz. .insert() metodi ichida yangi 
elementning indeksi va qiymati beriladi:'''

cars = ['Lacetti', 'Nexia 3', 'Cobalt','jentra','tiko','gelik']
cars.insert(20, 'Malibu') # 1-o'ringa yangi qiymat qo'shamiz
print(cars)

# ismlar = ['islombek','jobirhon','mahmudjon','isroil','muslima','rasulova','pokiza']
# ismlar.insert(5,'xusanboy')
# print(ismlar)

'''Elementni o'chirish
Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini bilishimiz lozim.
Inedks yordamida olib tashlash uchun "del" operatoridan foydalanamiz:'''

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1] # 2-element (anjir) ni o'chirib tashlaymiz
# del mevalar[2]
# print(mevalar)

'''Element qiymati bo'yichi o'chirish uchun
 esa .remove(qiymat) metodidan foydalanamiz. 
 Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz'''

# mevalar = ['shaftoli', 'anjir', 'shaftoli', "o'rik",'anor', 'olma']
# mevalar.remove('shaftoli') # Ro'yxatdan shaftolini o'chirdik
# print(mevalar)

'''.remove(qiymat) metodi ro'yxatda uchragan birinchi mos 
keluvchi qiymatni o'chiradi. Agar ro'yxatning ichida 2 va undan ko'p
 bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.'''

# hayvonlar = ['kuchik', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove("mushuk") # Ro'yxatda 2 ta mushuk bor, ulardan birinchisi o'chadi
# print(hayvonlar)

'''Elementni sug'urib olish
Ba'zida biror elementni butunlay o'chirib tashlash emas, 
balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi 
mumkin. Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz'''

# bozorlik = ["yog", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3) # Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ",bozorlik)


