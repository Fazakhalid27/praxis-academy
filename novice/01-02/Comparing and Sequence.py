#penggunaan append
'''buah = ['apel', 'jeruk', 'anggur']
buah.append('ceri')
print(buah)

#penggunaan extend
sayur = ['kol', 'bayam', 'wortel']
sayur_tambahan = ['sawi', 'tomat', 'kangkung']
sayur.extend(sayur_tambahan)
print(sayur)

#penggunaan insert
kendaraan = ['motor', 'kereta', 'pesawat']
kendaraan.insert(2, 'mobil')
print(kendaraan)

#penggunaan remove
sayur.remove('tomat')
print(sayur)

#pengunaan sort
buah.sort()
print(buah)

#queue
from collections import deque
queue = deque(["kinan", "anin", "aqila"])
queue.append('choerry')
queue.append('indah')
queue.popleft()
queue.popleft()

print(queue)'''

#penggunaan del
'''orang = ['ibu', 'ayah', 'anak']
del orang[:]
print(orang)'''

#Penggunaan sets
'''keranjang = {'bola', 'gundu', 'voli', 'bola'}
print('bola' in keranjang)

a = set('abracadabra')
b = set('alacazam')

print(a)
print(a -b)
print(a & b)
print(a ^ b)
print(a | b)'''

#dictionaries
'''info = {'nama':'Faza', 'Kota':'Jakarta', 'Hewan':'Kucing'}
print('Nama saya', info['nama'],
'saya tinggal di', info['Kota'],
'saya suka hewan', info['Hewan'])'''

#loop dict
'''knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)'''

'''for i in reversed(range(10,100,10)):
    print(i)'''

'''keranjang = ['apel', 'anggur', 'tomat', 'ceri', 'jeruk']
for i in sorted(keranjang):
    print(i)'''

