import random

xox = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
xox_sonra = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
corners = [1, 3, 7, 9]
kenar_orta = [2, 4, 6, 8]


def durum():
    print(' | '.join(xox_sonra[0]), "\n----------")
    print(' | '.join(xox_sonra[1]), "\n----------")
    print(' | '.join(xox_sonra[2]), "\n")


def yerler():
    global x_yerler, o_yerler
    x_yerler = []
    o_yerler = []

    for a in range(3):
        for i in range(3):
            if xox_sonra[a][i] == "X":
                x_yerler.append(a*3 + i + 1)
            elif xox_sonra[a][i] == "O":
                o_yerler.append(a*3 + i + 1)


def kim_kazandi():
    yerler()
    if (1 in x_yerler and 2 in x_yerler and 3 in x_yerler) or (4 in x_yerler and 5 in x_yerler and 6 in x_yerler) or (
            7 in x_yerler and 8 in x_yerler and 9 in x_yerler) or (
            1 in x_yerler and 4 in x_yerler and 7 in x_yerler) or (
            2 in x_yerler and 5 in x_yerler and 8 in x_yerler) or (
            3 in x_yerler and 6 in x_yerler and 9 in x_yerler) or (
            1 in x_yerler and 5 in x_yerler and 9 in x_yerler) or (7 in x_yerler and 5 in x_yerler and 3 in x_yerler):

        durum()
        print(f"\n(X) Kazandı")
        exit()

    if (1 in o_yerler and 2 in o_yerler and 3 in o_yerler) or (4 in o_yerler and 5 in o_yerler and 6 in o_yerler) or (
            7 in o_yerler and 8 in o_yerler and 9 in o_yerler) or (
            1 in o_yerler and 4 in o_yerler and 7 in o_yerler) or (
            2 in o_yerler and 5 in o_yerler and 8 in o_yerler) or (
            3 in o_yerler and 6 in o_yerler and 9 in o_yerler) or (
            1 in o_yerler and 5 in o_yerler and 9 in o_yerler) or (
            7 in o_yerler and 5 in o_yerler and 3 in o_yerler):

        durum()
        print(f"\n(O) Kazandı")
        exit()

    if kac_kere >= 9:
        durum()
        print("Berabere")
        exit()


def sayi_al(sayi_al_sayi):
    if sayi_al_sayi in xox[0]:
        for i in range(3):
            if sayi_al_sayi == xox[0][i]:
                return f"{xox_sonra[0][i]}"

    if sayi_al_sayi in xox[1]:
        for i in range(3):
            if sayi_al_sayi == xox[1][i]:
                return f"{xox_sonra[1][i]}"

    if sayi_al_sayi in xox[2]:
        for i in range(3):
            if sayi_al_sayi == xox[2][i]:
                return f"{xox_sonra[2][i]}"


def ilk_hamle():
    corner_random = random.choice(corners)
    if xox_sonra[1][1] == "X":
        if 1 <= corner_random <= 3:
            return xox[0][corner_random - 1]
        elif 4 <= corner_random <= 6:
            return xox[1][corner_random - 4]
        elif 7 <= corner_random <= 9:
            return xox[2][corner_random - 7]
    elif sayi_al(1) == "X" or sayi_al(3) == "X" or sayi_al(7) == "X" or sayi_al(9) == "X" or sayi_al(2) == "X" or sayi_al(4) == "X" or sayi_al(8) == "X" or sayi_al(6) == "X":
        return 5
    else:
        return random_secim()


def random_secim():
    olmayanlar = []
    for i in range(3):
        for a in range(3):
            if xox_sonra[i][a] == " ":
                olmayanlar.append(i*3 + a+1)

    return random.choice(olmayanlar)


flag = True
flag2 = True


def en_iyi():
    global flag, flag2
    if flag and ((sayi_al(1) == "X" and sayi_al(5) == "X" and sayi_al(9) == "O") or (sayi_al(1) == "O" and sayi_al(5) == "X" and sayi_al(9) == "X") or (sayi_al(3) == "X" and sayi_al(5) == "X" and sayi_al(7) == "O") or (sayi_al(3) == "O" and sayi_al(5) == "X" and sayi_al(7) == "X")) and kac_kere==3:
        flag = False
        olmayan_cornerlar = []
        if sayi_al(1) == " ": olmayan_cornerlar.append(1)
        if sayi_al(3) == " ": olmayan_cornerlar.append(3)
        if sayi_al(7) == " ": olmayan_cornerlar.append(7)
        if sayi_al(9) == " ": olmayan_cornerlar.append(9)
        return random.choice(olmayan_cornerlar)

    # iki tane o varsa (saldırı kazanma):
    # o'ler yan yanaysa
    if (sayi_al(1) == sayi_al(2) == "O") and sayi_al(3) != "X": return 3
    if (sayi_al(2) == sayi_al(3) == "O") and sayi_al(1) != "X": return 1
    if (sayi_al(4) == sayi_al(5) == "O") and sayi_al(6) != "X": return 6
    if (sayi_al(5) == sayi_al(6) == "O") and sayi_al(4) != "X": return 4
    if (sayi_al(7) == sayi_al(8) == "O") and sayi_al(9) != "X": return 9
    if (sayi_al(8) == sayi_al(9) == "O") and sayi_al(7) != "X": return 7

    if (sayi_al(1) == sayi_al(3) == "O") and sayi_al(2) != "X": return 2
    if (sayi_al(4) == sayi_al(6) == "O") and sayi_al(5) != "X": return 5
    if (sayi_al(7) == sayi_al(9) == "O") and sayi_al(8) != "X": return 8

    # o'ler alt altaysa
    if (sayi_al(1) == sayi_al(4) == "O") and sayi_al(7) != "X": return 7
    if (sayi_al(2) == sayi_al(5) == "O") and sayi_al(8) != "X": return 8
    if (sayi_al(3) == sayi_al(6) == "O") and sayi_al(9) != "X": return 9
    if (sayi_al(4) == sayi_al(7) == "O") and sayi_al(1) != "X": return 1
    if (sayi_al(5) == sayi_al(8) == "O") and sayi_al(2) != "X": return 2
    if (sayi_al(6) == sayi_al(9) == "O") and sayi_al(3) != "X": return 3

    if (sayi_al(1) == sayi_al(7) == "O") and sayi_al(4) != "X": return 4
    if (sayi_al(2) == sayi_al(8) == "O") and sayi_al(5) != "X": return 5
    if (sayi_al(3) == sayi_al(9) == "O") and sayi_al(6) != "X": return 6

    # o'ler çaprazsa
    if (sayi_al(1) == sayi_al(5) == "O") and sayi_al(9) != "X": return 9
    if (sayi_al(5) == sayi_al(9) == "O") and sayi_al(1) != "X": return 1
    if (sayi_al(7) == sayi_al(5) == "O") and sayi_al(3) != "X": return 3
    if (sayi_al(5) == sayi_al(3) == "O") and sayi_al(7) != "X": return 7

    if (sayi_al(1) == sayi_al(9) == "O") and sayi_al(5) != "X": return 5
    if (sayi_al(3) == sayi_al(7) == "O") and sayi_al(5) != "X": return 5

    # iki tane x varsa (savunma):
    # x'ler yan yanaysa
    if (sayi_al(1) == sayi_al(2) == "X") and sayi_al(3) != "O": return 3
    if (sayi_al(2) == sayi_al(3) == "X") and sayi_al(1) != "O": return 1
    if (sayi_al(4) == sayi_al(5) == "X") and sayi_al(6) != "O": return 6
    if (sayi_al(5) == sayi_al(6) == "X") and sayi_al(4) != "O": return 4
    if (sayi_al(7) == sayi_al(8) == "X") and sayi_al(9) != "O": return 9
    if (sayi_al(8) == sayi_al(9) == "X") and sayi_al(7) != "O": return 7

    if (sayi_al(1) == sayi_al(3) == "X") and sayi_al(2) != "O": return 2
    if (sayi_al(4) == sayi_al(6) == "X") and sayi_al(5) != "O": return 5
    if (sayi_al(7) == sayi_al(9) == "X") and sayi_al(8) != "O": return 8

    # x'ler alt altaysa
    if (sayi_al(1) == sayi_al(4) == "X") and sayi_al(7) != "O": return 7
    if (sayi_al(2) == sayi_al(5) == "X") and sayi_al(8) != "O": return 8
    if (sayi_al(3) == sayi_al(6) == "X") and sayi_al(9) != "O": return 9
    if (sayi_al(4) == sayi_al(7) == "X") and sayi_al(1) != "O": return 1
    if (sayi_al(5) == sayi_al(8) == "X") and sayi_al(2) != "O": return 2
    if (sayi_al(6) == sayi_al(9) == "X") and sayi_al(3) != "O": return 3

    if (sayi_al(1) == sayi_al(7) == "X") and sayi_al(4) != "O": return 4
    if (sayi_al(2) == sayi_al(8) == "X") and sayi_al(5) != "O": return 5
    if (sayi_al(3) == sayi_al(9) == "X") and sayi_al(6) != "O": return 6

    # x'ler çaprazsa
    if (sayi_al(1) == sayi_al(5) == "X") and sayi_al(9) != "O": return 9
    if (sayi_al(5) == sayi_al(9) == "X") and sayi_al(1) != "O": return 1
    if (sayi_al(7) == sayi_al(5) == "X") and sayi_al(3) != "O": return 3
    if (sayi_al(5) == sayi_al(3) == "X") and sayi_al(7) != "O": return 7

    if (sayi_al(1) == sayi_al(9) == "X") and sayi_al(5) != "O": return 5
    if (sayi_al(3) == sayi_al(7) == "X") and sayi_al(5) != "O": return 5

    if sayi_al(5) == "O" and (sayi_al(1) == "X" or sayi_al(3) == "X" or sayi_al(7) == "X" or sayi_al(9) == "X"):
        flag2 = False
        olmayan_edge = []
        if sayi_al(2) == " ": olmayan_edge.append(2)
        if sayi_al(4) == " ": olmayan_edge.append(4)
        if sayi_al(6) == " ": olmayan_edge.append(6)
        if sayi_al(8) == " ": olmayan_edge.append(8)
        return random.choice(olmayan_edge)


sira = "X"
kac_kere = 0
sayigir = 0
while True:
    kim_kazandi()
    durum()
    if sira == "X":
        if sayigir > 10:
            print("Kaybettiniz \n (O) Kazandı")
            exit()
        try:
            secim = int(input())
        except ValueError:
            print("Lütfen sayı giriniz")
            sayigir += 1
            continue
        if secim > 9 or sayi_al(secim) != " " or secim < 1:
            print("Lütfen 1 ile 9 arasında seçim yapınız ve dolu hücreyi denemeyiniz: ")
            continue
        sira2 = "X"
        sira = "O"
        kac_kere += 1
    elif sira == "O":
        if kac_kere == 1:
            secim = ilk_hamle()
        else:
            secim = en_iyi()
            if secim is None:
                secim = random_secim()

        print("Robotun seçtiği seçim: ", secim)
        sira = "X"
        sira2 = "O"
        kac_kere += 1

    if 1 <= int(secim) <= 3:
        xox_sonra[0][secim - 1] = sira2
    elif 4 <= int(secim) <= 6:
        xox_sonra[1][secim - 4] = sira2
    elif 7 <= int(secim) <= 9:
        xox_sonra[2][secim - 7] = sira2
