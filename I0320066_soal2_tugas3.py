dict1 = {'Nama':'Jefri','Hobi': ['Makan','Berenang','Traveling'],'Sosmed': ['IG : mjefri_s','Line : jefrys789','Wa : 081378882631']}
dict2 = {'Lagu kesukaan': ['Beautiful Scars','Painkiller','Say Im sorry'], 'Makanan kesukaan': ['Nasgor','Burger','Kebab']}
print("dict1['Nama']: ", dict1['Nama'])
print("dict1['Hobi']: ", dict1['Hobi'])
print("dict1['Sosmed']: ", dict1['Sosmed'])
print("dict2['Lagu kesukaan']: ", dict2['Lagu kesukaan'])
print("dict2['Makanan kesukaan']: ", dict2['Makanan kesukaan'])


dict1['Hobi'] = 'Membaca novel'
dict1['Sosmed'] = 'IG : myrhyme'
print("dict1['Hobi']: ", dict1['Hobi'])
print("dict1['Sosmed']: ", dict1['Sosmed'])

dict1['Hobi'] = 'Nonton film'
print("dict['Hobi']: ", dict1['Hobi'])

del dict2['Makanan kesukaan'][1:2]
dict2.clear()
del dict2


