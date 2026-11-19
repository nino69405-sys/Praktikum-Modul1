class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim

    def perkenalan(self):
        return f"Halo, saya {self.nama} dengan NIM {self.nim}"


# a. Class Dosen dengan atribut nama dan nidn
class Dosen:
    def __init__(self, nama, nidn):
        self.nama = nama
        self.nidn = nidn

    # b. Method ajar_mata_kuliah dengan parameter mata_kuliah
    def ajar_mata_kuliah(self, mata_kuliah):
        return f"{self.nama} (NIDN {self.nidn}) mengajar mata kuliah {mata_kuliah}"


# Pembuatan object Mahasiswa
mhs1 = Mahasiswa("Budi Santoso", "TI001")
mhs2 = Mahasiswa("Siti Aminah", "TI002")

print(mhs1.perkenalan())
print(mhs2.perkenalan())

# c. Instansiasi 2 object Dosen dan panggil methodnya
dosen1 = Dosen("Dr. Ahmad Fauzi", "0401018501")
dosen2 = Dosen("Rina Wulandari, M.Kom", "0412038802")

print(dosen1.ajar_mata_kuliah("Pemrograman Berorientasi Objek"))
print(dosen2.ajar_mata_kuliah("Basis Data"))\
    