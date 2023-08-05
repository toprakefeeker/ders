import random

liste = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

uzunluk = int(input("uzunluk ? "))

degisken2 = ""
for i in range(uzunluk):
    degisken1 = random.choice(liste)

    degisken2 += degisken1

print(degisken2)
