class ManajerInventori:
    def __init__(self):
        # Dictionary: kunci = nama barang, nilai = jumlah stok
        self.inventori = {}

    # a. Method tambah_barang (b. penambahan stok)
    def tambah_barang(self, nama, jumlah):
        if jumlah <= 0:
            return "Jumlah tambah harus positif"
        if nama in self.inventori:
            self.inventori[nama] += jumlah
        else:
            self.inventori[nama] = jumlah
        return f"Berhasil tambah {jumlah} {nama}. Stok: {self.inventori[nama]}"

    # a. Method hapus_barang (b. pengurangan stok)
    def hapus_barang(self, nama, jumlah):
        if nama not in self.inventori:
            return f"Barang {nama} tidak ada di inventori"
        if jumlah <= 0:
            return "Jumlah hapus harus positif"
        if jumlah > self.inventori[nama]:
            return f"Stok {nama} tidak mencukupi (stok: {self.inventori[nama]})"
        self.inventori[nama] -= jumlah
        if self.inventori[nama] == 0:
            del self.inventori[nama]
            return f"Berhasil hapus {jumlah} {nama}. Stok habis, barang dihapus dari inventori"
        return f"Berhasil hapus {jumlah} {nama}. Stok: {self.inventori[nama]}"

    # a. Method lihat_inventori
    def lihat_inventori(self):
        if not self.inventori:
            return "Inventori kosong"
        hasil = "Daftar inventori:"
        for nama, stok in self.inventori.items():
            hasil += f"\n- {nama}: {stok}"
        return hasil


# c. Demonstrasi semua method
manajer = ManajerInventori()

print(manajer.lihat_inventori())
print(manajer.tambah_barang("Pensil", 50))
print(manajer.tambah_barang("Buku Tulis", 30))
print(manajer.tambah_barang("Pensil", 20))
print(manajer.tambah_barang("Penghapus", -5))
print(manajer.lihat_inventori())

print(manajer.hapus_barang("Pensil", 15))
print(manajer.hapus_barang("Buku Tulis", 100))
print(manajer.hapus_barang("Spidol", 5))
print(manajer.hapus_barang("Buku Tulis", 30))
print(manajer.lihat_inventori())