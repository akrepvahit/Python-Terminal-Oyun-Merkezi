import random
import time
import math

class Renkler:
    HEADER = '\033[95m'
    MAVI = '\033[94m'
    CYAN = '\033[96m'
    YESIL = '\033[92m'
    SARI = '\033[93m'
    KIRMIZI = '\033[91m'
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class AkilliTahminBotu:
    DUSUNME_MESAJLARI = ["🤔 Hmmm, düşünüyorum...", "🧠 Beyin fırtınası yapıyorum...", "⚙️ Çarklar dönüyor...", "⏳ Bir saniye, hesaplıyorum..."]
    YUKARI_TAHMIN_MESAJLARI = ["📈 Anlaşıldı, daha yukarı çıkıyorum!", "Yukarı demek... Tamamdır!", "Hedefi yükseltiyorum!"]
    ASAGI_TAHMIN_MESAJLARI = ["📉 Rotayı aşağı çeviriyorum!", "Daha düşük bir sayı, not aldım.", "Aşağısı için dalışa geçiyorum!"]

    def __init__(self, min_sayi: int = 1, max_sayi: int = 100):
        self.min_sayi = min_sayi
        self.max_sayi = max_sayi
        self.resetle()

    def resetle(self):
        self.en_dusuk_sinir = self.min_sayi
        self.en_yuksek_sinir = self.max_sayi
        self.deneme_sayisi = 0
        self.tahmin = 0
        
    def basla(self):
        self._oyun_girisi()

        while True:
            self.deneme_sayisi += 1

            if self.en_dusuk_sinir > self.en_yuksek_sinir:
                print(f"\n{Renkler.KIRMIZI}{Renkler.BOLD}🧐 Hmmm... Bir çelişki var. Sanırım bana yanlış ipucu verdin. Oyunu bozdun!{Renkler.RESET}")
                break

            print(f"\n{Renkler.SARI}{random.choice(self.DUSUNME_MESAJLARI)}{Renkler.RESET}")
            time.sleep(random.uniform(0.5, 1.5))

            self.tahmin = (self.en_dusuk_sinir + self.en_yuksek_sinir) // 2

            print(f"💥 {Renkler.BOLD}Deneme {self.deneme_sayisi}:{Renkler.RESET} Tahminim... {Renkler.CYAN}{self.tahmin}!{Renkler.RESET}")

            geri_bildirim = self._kullanici_geri_bildirimi_al()

            if geri_bildirim == 'b':
                self._zafer_mesaji()
                break
            elif geri_bildirim == 'y':
                print(f"{Renkler.MAVI}{random.choice(self.YUKARI_TAHMIN_MESAJLARI)}{Renkler.RESET}")
                self.en_dusuk_sinir = self.tahmin + 1
            elif geri_bildirim == 'd':
                print(f"{Renkler.MAVI}{random.choice(self.ASAGI_TAHMIN_MESAJLARI)}{Renkler.RESET}")
                self.en_yuksek_sinir = self.tahmin - 1

    def _oyun_girisi(self):
        print(f"{Renkler.HEADER}==================================================={Renkler.RESET}")
        print(f"   {Renkler.BOLD}🤖 CANAVAR SEVİYE SAYI TAHMİN BOTU 🤖{Renkler.RESET}   ")
        print(f"{Renkler.HEADER}==================================================={Renkler.RESET}")
        print(f"Aklından {Renkler.BOLD}{self.min_sayi}{Renkler.RESET} ile {Renkler.BOLD}{self.max_sayi}{Renkler.RESET} arasında bir sayı tut.")
        print(f"Ben de onu {Renkler.UNDERLINE}en az denemede{Renkler.RESET} bulmaya çalışacağım. Görelim bakalım!")
        input(f"{Renkler.SARI}Hazır olduğunda Enter'a bas...{Renkler.RESET}")

    def _kullanici_geri_bildirimi_al(self) -> str:
        while True:
            geri_bildirim = input(
                f"\nEğer tahminim doğruysa {Renkler.YESIL}'B'{Renkler.RESET} (Bildin!),\n"
                f"tuttuğun sayı daha {Renkler.CYAN}YÜKSEKSE 'Y'{Renkler.RESET},\n"
                f"daha {Renkler.CYAN}DÜŞÜKSE 'D'{Renkler.RESET} gir: "
            ).lower()

            if geri_bildirim in ['y', 'd', 'b']:
                return geri_bildirim
            else:
                print(f"\n{Renkler.KIRMIZI}🚨 Geçersiz komut! Lütfen sadece 'Y', 'D' veya 'B' harflerinden birini gir.{Renkler.RESET}")

    def _zafer_mesaji(self):
        print(f"\n{Renkler.YESIL}{Renkler.BOLD}🎉 YAŞASIN! {self.deneme_sayisi}. denemede sayını ({self.tahmin}) buldum!{Renkler.RESET}")
        
        optimal_deneme = math.ceil(math.log2(self.max_sayi - self.min_sayi + 1))
        print(f"{Renkler.SARI}Bu arada, bu aralık için teorik olarak en iyi sonuç {optimal_deneme} denemedir.{Renkler.RESET}")

        if self.deneme_sayisi <= optimal_deneme:
            print(f"{Renkler.YESIL}Gördüğün gibi, optimum sürede çözdüm. Zekama hayran kaldın, değil mi? 😎{Renkler.RESET}")
        else:
            print(f"{Renkler.SARI}Biraz yavaş kaldım ama bunun sebebi sensin, yeterince hızlı cevap vermedin! 😉{Renkler.RESET}")


class KullaniciTahminOyunu:
    def __init__(self, min_sayi: int = 1, max_sayi: int = 100):
        self.min_sayi = min_sayi
        self.max_sayi = max_sayi
        self.gizli_sayi = random.randint(self.min_sayi, self.max_sayi)
        self.deneme_sayisi = 0

    def basla(self):
        print(f"\n{Renkler.HEADER}--- SAYI TAHMİN OYUNU (SEN TAHMİN ET) ---{Renkler.RESET}")
        print(f"{Renkler.MAVI}Harika! {self.min_sayi} ile {self.max_sayi} arasında bir sayı tuttum.{Renkler.RESET}")
        print("Bakalım kaç denemede bulabileceksin?")

        while True:
            try:
                tahmin_str = input(f"\n{Renkler.BOLD}Tahminin nedir?: {Renkler.RESET}")
                tahmin = int(tahmin_str)
                self.deneme_sayisi += 1
            except ValueError:
                print(f"{Renkler.KIRMIZI}Lütfen sadece sayısal bir değer gir.{Renkler.RESET}")
                continue

            if tahmin < self.gizli_sayi:
                print(f"{Renkler.SARI}Daha YÜKSEK bir sayı söylemelisin! ⬆️{Renkler.RESET}")
            elif tahmin > self.gizli_sayi:
                print(f"{Renkler.SARI}Daha DÜŞÜK bir sayı söylemelisin! ⬇️{Renkler.RESET}")
            else:
                print(f"\n{Renkler.YESIL}{Renkler.BOLD}🎉 TEBRİKLER! {self.deneme_sayisi}. denemede doğru sayıyı ({self.gizli_sayi}) buldun!{Renkler.RESET}")
                break


class KelimeBulmaca:
    KELIME_LISTESI = ["python", "türkiye", "kodlama", "yapayzeka", "proje", "canavar", "eglence", "klavye", "monitor", "telefon", "bilgisayar", "programlama", "vatan" , "ankara", "istanbul", "malatya", "şanlıurfa", "uşak", "kocaeli", "gümüşhane", "balıkesir", "ahmet", "mehmet"]
    ADAM_ASMACI_GORSELLERI = [
        """
           +---+
           |   |
               |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
               |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
           |   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|   |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
               |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          /    |
               |
        =========
        """,
        """
           +---+
           |   |
           O   |
          /|\\  |
          / \\  |
               |
        =========
        """
    ]

    def __init__(self):
        self.secilen_kelime = random.choice(self.KELIME_LISTESI)
        self.kalan_hak = 6
        self.tahmin_edilen_harfler = set()
        self.gosterilen_kelime = ["_"] * len(self.secilen_kelime)

    def _oyun_durumunu_goster(self):
        print(f"{Renkler.SARI}{self.ADAM_ASMACI_GORSELLERI[6 - self.kalan_hak]}{Renkler.RESET}")
        print(f"{Renkler.CYAN}Kelime: {' '.join(self.gosterilen_kelime)}{Renkler.RESET}")
        print(f"{Renkler.MAVI}Kalan Hak: {self.kalan_hak}{Renkler.RESET}")
        print(f"{Renkler.MAVI}Tahmin Edilen Harfler: {', '.join(sorted(self.tahmin_edilen_harfler))}{Renkler.RESET}")

    def basla(self):
        print(f"\n{Renkler.HEADER}--- KELİME BULMACA OYUNUNA HOŞ GELDİN ---{Renkler.RESET}")
        
        while self.kalan_hak > 0 and "_" in self.gosterilen_kelime:
            self._oyun_durumunu_goster()
            tahmin = input(f"{Renkler.BOLD}Bir harf tahmin et: {Renkler.RESET}").lower()

            if len(tahmin) != 1 or not tahmin.isalpha():
                print(f"{Renkler.KIRMIZI}Geçersiz giriş! Lütfen sadece bir harf gir.{Renkler.RESET}")
                continue
            
            if tahmin in self.tahmin_edilen_harfler:
                print(f"{Renkler.SARI}Bu harfi zaten tahmin ettin! Başka bir harf dene.{Renkler.RESET}")
                continue

            self.tahmin_edilen_harfler.add(tahmin)

            if tahmin in self.secilen_kelime:
                print(f"{Renkler.YESIL}Doğru tahmin! '{tahmin}' harfi kelimede var.{Renkler.RESET}")
                for i, harf in enumerate(self.secilen_kelime):
                    if harf == tahmin:
                        self.gosterilen_kelime[i] = harf
            else:
                print(f"{Renkler.KIRMIZI}Yanlış tahmin! '{tahmin}' harfi kelimede yok.{Renkler.RESET}")
                self.kalan_hak -= 1
        
        self._oyun_durumunu_goster()
        if "_" not in self.gosterilen_kelime:
            print(f"\n{Renkler.YESIL}{Renkler.BOLD}🎉 TEBRİKLER! Kelimeyi buldun: {self.secilen_kelime.upper()}{Renkler.RESET}")
        else:
            print(f"\n{Renkler.KIRMIZI}{Renkler.BOLD}GAME OVER! ☠️ Bilemedin. Doğru kelime: {self.secilen_kelime.upper()}{Renkler.RESET}")


def sayi_tahmin_alt_menu():
    print(f"\n{Renkler.HEADER}--- Sayı Tahmin Oyunu Modu Seç ---{Renkler.RESET}")
    print(f"{Renkler.CYAN}1.{Renkler.RESET} Ben sayı tutacağım, sen tahmin et (Bilgisayar Tahmin Eder)")
    print(f"{Renkler.CYAN}2.{Renkler.RESET} Sen sayı tut, ben tahmin edeyim (Kullanıcı Tahmin Eder)")

    while True:
        secim = input(f"\n{Renkler.BOLD}Hangi modu oynamak istersin? (1-2): {Renkler.RESET}")
        if secim in ["1", "2"]:
            return secim
        else:
            print(f"{Renkler.KIRMIZI}Geçersiz seçim! Lütfen 1 veya 2 gir.{Renkler.RESET}")

def ana_menu():
    print(f"\n{Renkler.HEADER}====================================={Renkler.RESET}")
    print(f"  {Renkler.BOLD}🤖 OYUN MERKEZİNE HOŞ GELDİN 🤖{Renkler.RESET}  ")
    print(f"{Renkler.HEADER}====================================={Renkler.RESET}")
    print(f"{Renkler.CYAN}1.{Renkler.RESET} Sayı Tahmin Oyunu")
    print(f"{Renkler.CYAN}2.{Renkler.RESET} Kelime Bulmaca")
    print(f"{Renkler.CYAN}3.{Renkler.RESET} Çıkış")
    
    while True:
        secim = input(f"\n{Renkler.BOLD}Oynamak istediğin oyunun numarasını gir (1-3): {Renkler.RESET}")
        if secim in ["1", "2", "3"]:
            return secim
        else:
            print(f"{Renkler.KIRMIZI}Geçersiz seçim! Lütfen 1, 2 veya 3 gir.{Renkler.RESET}")

def main():
    while True:
        secim = ana_menu()

        if secim == '1':
            mod_secimi = sayi_tahmin_alt_menu()
            if mod_secimi == '1':
                oyun = AkilliTahminBotu(1, 100)
                oyun.basla()
            else:
                oyun = KullaniciTahminOyunu(1, 100)
                oyun.basla()
        elif secim == '2':
            oyun = KelimeBulmaca()
            oyun.basla()
        elif secim == '3':
            print(f"\n{Renkler.MAVI}Oyun merkezinden ayrılıyorsun. Tekrar görüşmek üzere! 👋{Renkler.RESET}")
            break
        
        input(f"\n{Renkler.SARI}Ana menüye dönmek için Enter'a bas...{Renkler.RESET}")


if __name__ == "__main__":
    main()