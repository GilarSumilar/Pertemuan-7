# Praktikum7

## Profil
| Variable | Isi |
| -------- | --- |
| **Nama** | Gilar Sumilar |
| **NIM** | 312210407 |
| **Kelas** | TI.22.A.4 |
| **Mata Kuliah** | Bahasa Pemrograman |

## Tugas struktur kondisi 
1. Latihan 1
- Buat program sederhada dengan input 2 buah bilangan, kemudian
  tentukan bilangan terbesar dari kedua bilangan tersebut
  menggunakan statement if.
 
 ```Python
#Masukan input 
bil1 = int (input("Masukan bilangan : "))
bil2 = int (input("Masukan bilangan : "))

#Nilai terbesar

if (bil1 > bil2):
    print("Bilangan terbesar :",bil1)

#Nilai terkecil

if (bil1 < bil2):
    print("Bilangan terbesar :",bil2)
```
## Hasil program
![1](Gambar/Gambar1.png)

2. Latihan 2
- Buat program untuk mengurutkan data berdasarkan input sejumlah
  data (minimal 3 variable input atau lebih), kemudian tampilkan
  hasilnya secara berurutan mulai dari data terkecil.
 
 ```Python
#Masukan inputan
bil1 = int(input("Bilangan ke-1: "))
bil2 = int(input("Bilangan ke-2: "))
bil3 = int(input("Bilangan ke-3: "))

#Buat variable data
data = [bil1, bil2, bil3]

#Menampilkan data
print("Data sebelum di urutkan :", data)
list.sort(data)
print("Data setelah di urutkan :", data)
```

`list.sort` Syntax ini berfungsi untuk mengurutkan data

## Hasil program
![2](Gambar/Gambar2.png)

## Tugas perulangan
1. Latihan 1
*Buat program dengan perulangan bertingkat (nested) for yang 
menghasilkan output sebagai berikut:

```Python
baris = 10
kolom = baris

for bar in range(baris):
    for col in range(kolom):
        tab = bar+col
        print("{0:>5}".format(tab), end='')
    print()
```

Penjelasan

1. Pendeklarasian variable
```python
baris = 10
kolom = baris
```

2. Untuk perulangan baris dan kolom menggunakan `for`
```python
for bar in range(baris):
    for col in range(kolom):
        tab = bar+col        
```
3. Untuk menampikan hasil dari perulangan
     * Agar terlihat rapih menggunakan `format string` rata ke kanan sebanyak 5 karakter
     * Agar tidak membuat baris baru menggunakan `end=''` (baris)
     * Penggunaan `print()` untuk membuat baris baru (kolom)
```python
  print("{0:>5}".format(tab), end='')
print()    
```

