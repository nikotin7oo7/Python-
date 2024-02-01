car_0 = {'model':'ferari','rang':'qizil'}
print(car_0['model'])
car_0['iy'] = 2023
print(car_0['iy'])
talaba_1 = {}

del car_0['model']
print(car_0)

telefonlar = {
    'model':'Samsung',
    'yil':2014,
    'ram':'12GB',
    'rom':'256GB'
}

print(f"Telefonning modeli {telefonlar['model']}")
phone = telefonlar.get('sam','Bunday model yoq')
print(phone)
