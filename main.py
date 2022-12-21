def kare(k):
    print("Karenin alanı = {}".format(k * k))


def dikdortgen(k, u):
    print("Dikdörtgenin alanı = {}".format(k * u))
    
def daire(pi,r):
    print("Dairenin alanı = {}".format((pi)*(r^2)))

if __name__ == '__main__':
    print("""
    1 - Kare
    2 - Dikdörtgen
    3 - Daire
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
        pi = 3.14
        r = float(input("Yarı çap giriniz: "))
        daire(pi,r)

    else:
        print("Sadece belirtilen sayılardan birini giriniz.")
