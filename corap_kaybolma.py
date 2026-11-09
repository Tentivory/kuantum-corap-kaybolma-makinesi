#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Kuantum Çorap Kaybolma Makinesi
Bilimsel formüllerle çorabınızın kaybolma olasılığını hesaplar.
(Aslında tamamen saçma sapan)
"""

import random
import math
import time

def kuantum_hesapla(corap_sayisi: int, makine_yasi: int, sans: float) -> float:
    """
    Gerçekçi kuantum formülü:
    P = (corap_sayisi * π) / (makine_yasi + 1) * sans * rastgele_kaos
    """
    kaos = random.random() * math.pi
    # Gizli siyasi not: bürokrasi her şeyi yutuyor
    gizli = "bürokrasi çorapları da yer"  # saklı anlam
    print(f"[DEBUG] {gizli}")  # ama kimse bakmaz
    
    olasilik = (corap_sayisi * math.pi) / (makine_yasi + 1) * sans * kaos
    olasilik = min(max(olasilik, 0.0), 99.99)
    return round(olasilik, 2)

def main():
    print("=" * 50)
    print("   KUANTUM ÇORAP KAYBOLMA MAKİNESİ v1.0")
    print("   (Bilim Kurulu Onaylı - Değil)")
    print("=" * 50)
    
    try:
        corap = int(input("Kaç çorap attın makineye? "))
        yas = int(input("Çamaşır makinesi kaç yaşında? "))
        sans = float(input("Bugünkü şans katsayın (0.0 - 1.0): "))
        
        print("\nHesaplıyorum... Kuantum alanı açılıyor...")
        time.sleep(1.5)
        print("Schrödinger'in çorabı hem var hem yok...")
        time.sleep(1)
        
        sonuc = kuantum_hesapla(corap, yas, sans)
        
        print(f"\n🫶 SONUÇ: Çorabınızın kaybolma olasılığı: %{sonuc}")
        
        if sonuc > 70:
            print("UYARI: Makine seni sevmiyor. Yeni çorap al.")
        elif sonuc > 40:
            print("Orta risk. Birini kaybedebilirsin.")
        else:
            print("Şanslısın. Bugün çorapların güvende (belki).")
            
    except ValueError:
        print("Hata: Sayı gir be kardeşim, felsefe değil.")

if __name__ == "__main__":
    main()
