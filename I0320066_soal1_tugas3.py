list1 = ['Rengga','Afnan','Rahmat','Naufal','Nurki','Aji','Alam','Rio','Memed','Raka']

print("list1[0:9]: ", list1[0:9])
print("Nilai ada pada index 4: ", list1[4])
print("Nilai ada pada index 6: ", list1[6])
print("Nilai ada pada index 7: ", list1[7])

list1[3] = 'Erika'
print("Nilai baru ada pada index 3: ", list1[3])
list1[5] = 'Laras'
print("Nilai baru ada pada index 5: ", list1[5])
list1[9] = 'Efa'
print("Nilai baru ada pada index 9: ", list1[9])

list1.append('Bima')
list1.append('Puguh')

print(['Rengga']*2)
print(['Afnan']*3)
print(['Rahmat']*4)
print(['Naufal']*5)
print(['Nurki']*6)
print(['Aji']*5)
print(['Alam']*4)
print(['Rio']*3)
print(['Memed']*2)
print(['Raka']*2)

print(len(list1))