# main.py

from Oyun import TasKagitMakas

if __name__ == "__main__":
    hedef = int(input("Oyun kaç puanda bitsin? --> "))
    oyun = TasKagitMakas(hedef)
    oyun.baslat()
