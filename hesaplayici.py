from math import isclose, isfinite


def main():
    print("Seyir ve Yedek Yakıt Hesaplayıcısı")

    try:
        # input() metin döndürür. Süreleri tam sayıya dönüştür.
        seyir_metni = input("Seyir süresi (dk): ")
        seyir_dk = int(seyir_metni)
        yedek_dk = int(input("Yedek süre (dk): "))

        # Yakıt değerlerinde nokta veya virgül kullanılabilir.
        tuketim = float(input("Saatlik tüketim (L/sa): ").replace(",", "."))
        mevcut = float(input("Mevcut yakıt (L): ").replace(",", "."))
    except ValueError:
        print("Geçersiz girdi. Süreler tam sayı, yakıt değerleri sayı olmalı.")
        return

    if (seyir_dk < 0 or yedek_dk < 0 or tuketim <= 0 or mevcut < 0
            or not isfinite(tuketim) or not isfinite(mevcut)):
        print("Geçersiz girdi. Süreler ve yakıt negatif olamaz.")
        print("Tüketim pozitif olmalı, yakıt değerleri sonlu olmalı.")
        return

    # Dakikayı saate çevirip her bölümün yakıtını hesapla.
    seyir = (seyir_dk / 60) * tuketim
    yedek = (yedek_dk / 60) * tuketim
    toplam = seyir + yedek
    fark = mevcut - toplam

    # float kaynaklı çok küçük farkları eşitlik olarak değerlendir.
    esit = isclose(fark, 0, abs_tol=1e-9)
    yeterli = mevcut >= toplam or esit  # bool
    durum = "yeterli" if yeterli else "yetersiz"

    print(f"Seyir yakıtı: {seyir:.2f} L")
    print(f"Yedek yakıt: {yedek:.2f} L")
    print(f"Toplam yakıt: {toplam:.2f} L")
    print(f"Mevcut yakıt, bu hesaba göre {durum}.")
    print(f"Mevcut yakıt − toplam: {0.0 if esit else fark:+.2f} L")


if __name__ == "__main__":
    main()
