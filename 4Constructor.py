class Kendaraan:
    # a. Class attribute
    bahan_bakar = "Bensin"

    # b. Constructor untuk inisialisasi merk, warna, dan tahun
    def __init__(self, merk, warna, tahun):
        # Instance attributes
        self.merk = merk
        self.warna = warna
        self.tahun = tahun

    def info_kendaraan(self):
        return f"{self.merk} warna {self.warna} tahun {self.tahun}, bahan bakar {self.bahan_bakar}"


# Instansiasi object
kendaraan1 = Kendaraan("Toyota Avanza", "Hitam", 2020)
kendaraan2 = Kendaraan("Honda Beat", "Merah", 2022)

print(kendaraan1.info_kendaraan())
print(kendaraan2.info_kendaraan())

# c. Demonstrasi akses instance attribute dan class attribute
print("\n=== Instance attribute (hanya lewat object, nilainya beda tiap object) ===")
print(f"Merk kendaraan1: {kendaraan1.merk}")
print(f"Merk kendaraan2: {kendaraan2.merk}")

print("\n=== Class attribute (bisa lewat class maupun object, nilainya sama) ===")
print(f"Lewat class      : {Kendaraan.bahan_bakar}")
print(f"Lewat kendaraan1 : {kendaraan1.bahan_bakar}")
print(f"Lewat kendaraan2 : {kendaraan2.bahan_bakar}")

print("\n=== Ubah class attribute lewat class (berlaku untuk semua object) ===")
Kendaraan.bahan_bakar = "Pertalite"
print(f"kendaraan1: {kendaraan1.bahan_bakar}")
print(f"kendaraan2: {kendaraan2.bahan_bakar}")

print("\n=== Ubah lewat object (hanya berlaku untuk object itu) ===")
kendaraan1.bahan_bakar = "Solar"
print(f"kendaraan1: {kendaraan1.bahan_bakar}")
print(f"kendaraan2: {kendaraan2.bahan_bakar}")
print(f"Kendaraan : {Kendaraan.bahan_bakar}")