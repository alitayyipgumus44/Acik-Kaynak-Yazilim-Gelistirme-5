def kare(k):
    print("Karenin alanı = {}".format(k * k))


def dikdortgen(k, u):
    print("Dikdörtgenin alanı = {}".format(k * u))
    
def ucgenin_alanı(taban, h):
    print(f"Üçgenin alanı {taban * h / 2}")

if __name__ == '__main__':
    print("""
    1 - Kare
    2 - Dikdörtgen
    3 - Üçgen
    """)

    secim = int(input("Alanını hesaplamak istediğiniz şekil: "))

    if secim == 1:
        k = int(input("Karenin bir kenarı: "))
        kare(k)

    elif secim == 2:
        k = int(input("Dikdörtgenin kısa kenarı: "))
        u = int(input("Dikdörtgenin uzun kenarı: "))
        dikdortgen(k, u)

    elif secim == 3:
        t = int(input("Taban Girin : "))
        h = int(input("Yükseklik girin : "))
        ucgenin_alanı(t, h)
                

    else:
        print("Sadece belirtilen sayılardan birini giriniz.")
