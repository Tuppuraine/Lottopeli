from random import randint
rivi = []
arvottu_rivi = []
oikein = 0

while len(rivi) <= 6:
    try:
        numero = int(input("Anna lottorivin numero välillä 1-42: "))
        if numero not in range(0,42):
            print("Voit antaa numeron vain välillä 0-42")
        elif numero not in rivi:
            rivi.append(numero)
        elif numero in rivi:
            print("Et voi antaa samaa numeroa kahdesti")
    except ValueError:
        print("Voit antaa vain numeroita")

while len(arvottu_rivi) <= 6:
    arvonta = randint(0, 42)
    if arvonta not in arvottu_rivi:
        arvottu_rivi.append(arvonta)

for numero in rivi:
    if numero in arvottu_rivi:
        oikein += 1

print(f"arvottu rivi oli: {arvottu_rivi}, sinun rivisi oli {rivi}. Sait {oikein} oikein.")
