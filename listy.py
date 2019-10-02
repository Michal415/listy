imiona = []
while True:
    print("Podaj imie kota" +str(len(imiona)+1) + "Ewntualnie nic nie wpisuj ;) aby zakonczyc")
    imie = input()
    if imie =='':
        break
    imiona = imiona + [imie]
print("oto imiona:")
for imi in imiona:
    print(imi)
