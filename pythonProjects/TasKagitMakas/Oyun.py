# oyun.py

import random

class TasKagitMakas:
    def __init__(self, hedef_puan):
        self.hedef_puan = hedef_puan
        self.b_skor = 0
        self.o_skor = 0
        self.hamleler = ["t", "k", "m"]

    def baslat(self):
        print("Taş-Kağıt-Makas oyununa hoşgeldiniz!")
        while self.o_skor < self.hedef_puan and self.b_skor < self.hedef_puan:
            b_hamle = random.choice(self.hamleler)
            o_hamle = input("(t=taş, k=kağıt, m=makas) Hamlenizi giriniz --> ").strip().lower()
            print("Bilgisayarın hamlesi:", b_hamle)

            if o_hamle not in self.hamleler:
                print("Geçerli bir hamle giriniz!")
                continue

            if b_hamle == o_hamle:
                print("Berabere!")
            elif (b_hamle == "t" and o_hamle == "m") or (b_hamle == "k" and o_hamle == "t") or (b_hamle == "m" and o_hamle == "k"):
                print("Kaybettiniz!")
                self.b_skor += 1
            else:
                print("Kazandınız!")
                self.o_skor += 1

            print(f"Skor: Oyuncu {self.o_skor} - Bilgisayar {self.b_skor}")

        if self.o_skor == self.hedef_puan:
            print("Tebrikler, kazandınız! 😊")
        else:
            print("Üzgünüm, bilgisayar kazandı. 😞")
