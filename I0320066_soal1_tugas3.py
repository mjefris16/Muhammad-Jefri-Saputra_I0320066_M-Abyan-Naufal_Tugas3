list1 = ['Rengga','Afnan','Rahmat','Naufal','Nurki','Aji','Alam','Rio','Memed','Raka']

print("list1[0:9]: ", list1[0:9])
print("Nama teman pada index 4: ", list1[4])
print("Nama teman pada index 6: ", list1[6])
print("Nama teman pada index 7: ", list1[7])

list1[3] = 'Erika'
print("Nama teman baru ada pada index 3: ", list1[3])
list1[5] = 'Laras'
print("Nama teman baru ada pada index 5: ", list1[5])
list1[9] = 'Efa'
print("Nama teman baru ada pada index 9: ", list1[9])

list1.append('Bima')
list1.append('Puguh')

print(list1)

for teman in list1:
    print("Perulangan nama teman: ", teman)

Panjang_list = len(list1)
print("Panjang list teman: ", Panjang_list)