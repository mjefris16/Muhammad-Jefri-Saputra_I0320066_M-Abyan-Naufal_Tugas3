dict1 = {'Nama':'Jefri','Hobi 1': 'Makan','Hobi 2': 'Berenang','Hobi 3': 'Traveling','Sosmed 1': 'IG : mjefri_s','Sosmed 2': 'Line : jefrys789','Sosmed 3': 'Wa : 081378882631'}
dict2 = {'Lagu kesukaan 1': 'Beautiful Scars', 'Lagu kesukaan 2': 'Painkiller', 'Lagu kesukaan 3': 'Say Im sorry', 'Makanan kesukaan 1': 'Nasgor', 'Makanan kesukaan 2': 'Burger', 'Makanan kesukaan 3': 'Kebab'}
print("dict1['Nama']: ", dict1['Nama'])
print("dict1['Hobi 1']: ", dict1['Hobi 1'])
print("dict1['Hobi 2']: ", dict1['Hobi 2'])
print("dict1['Hobi 3']: ", dict1['Hobi 3'])
print("dict1['Sosmed 1']: ", dict1['Sosmed 1'])
print("dict1['Sosmed 2']: ", dict1['Sosmed 2'])
print("dict1['Sosmed 3']: ", dict1['Sosmed 3'])
print("dict2['Lagu kesukaan 1']: ", dict2['Lagu kesukaan 1'])
print("dict2['Lagu kesukaan 2']: ", dict2['Lagu kesukaan 2'])
print("dict2['Lagu kesukaan 3']: ", dict2['Lagu kesukaan 3'])
print("dict2['Makanan kesukaan 1']: ", dict2['Makanan kesukaan 1'])
print("dict2['Makanan kesukaan 2']: ", dict2['Makanan kesukaan 2'])
print("dict2['Makanan kesukaan 3']: ", dict2['Makanan kesukaan 3'])

dict1['Hobi 2'] = 'Membaca novel'
dict1['Sosmed 3'] = 'IG : myrhyme'
print("dict1['Hobi 2]: ", dict1['Hobi 2'])
print("dict1['Sosmed 3']: ", dict1['Sosmed 3'])

dict1['Hobi 4'] = 'Nonton film'
print("dict['Hobi 4]: ", dict1['Hobi 4'])

del dict2['Makanan kesukaan 2']
del dict2['Makanan kesukaan 3']
dict2.clear()
del dict2

