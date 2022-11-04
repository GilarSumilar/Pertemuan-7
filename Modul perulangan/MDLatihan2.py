print("===============================")
print("===Mencari bilangan terbesar===")
print("===============================\n")

max = 0
while True:
    a = int(input("Masukan bilangan :"))
    if max < a:
        max = 0
    if a == 0:
        break

print("Bilangan terbesar adalah :", max)