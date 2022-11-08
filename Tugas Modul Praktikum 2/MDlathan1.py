a = int(input("Masukan bilangan ke-1 :"))
b = int(input("Masukan bilangan ke-2 :"))
c = int(input("Masukan bilangan ke-3 :"))

max = a

if b > max:
    max = b

if c > max:
    max = c

print()
print("Nilai terbesar :", max)