def kare(k):
    print("Karenin alanı = {}".format(k * k))


def dikdortgen(k, u):
    print("Dikdörtgenin alanı = {}".format(k * u))

if __name__ == '__main__':
    print("""
    1 - Kare
    2 - Dikdörtgen
    """)

    secim = int(input("Alanını hesaplamak istediğiniz şekil: "))

    if secim == 1:
        k = int(input("Karenin bir kenarı: "))
        kare(k)

    elif secim == 2:
        k = int(input("Dikdörtgenin kısa kenarı: "))
        u = int(input("Dikdörtgenin uzun kenarı: "))
        dikdortgen(k, u)

    else:
        print("Sadece belirtilen sayılardan birini giriniz.")
