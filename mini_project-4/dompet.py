class Dompet:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo = saldo
        self.riwayat = []
        
        
    def setor(self, jumlah):
        if jumlah <= 0:
            print("Jumlah setoran harus diatas 0!\n")
            return
            
        self.saldo += jumlah
        print(f"Setoran Rp{jumlah:,} berhasil.")
        print(f"Total saldo {self.pemilik}: Rp{self.saldo:,}.\n")
        self.riwayat.append(
            {
                "jenis": "setor",
                "jumlah": jumlah
            }
        )
        
        
    def tarik(self, jumlah):
        if jumlah <= 0:
            print("Jumlah penarikan harus diatas 0!\n")
            return
            
        if jumlah > self.saldo:
            print(f"Saldo tidak cukup untuk penarikan Rp{jumlah:,}!")
            print(f"Saldo {self.pemilik}: Rp{self.saldo:,}.\n")
            return
            
        self.saldo -= jumlah
        print(f"Penarikan Rp{jumlah:,} berhasil.")
        print(f"Sisa saldo {self.pemilik}: Rp{self.saldo:,}.\n")
        self.riwayat.append(
            {
                "jenis": "tarik",
                "jumlah": jumlah
            }
        )
    
    
    def lihat_riwayat(self):
        print(f"Riwayat {self.pemilik}:")
        for i, item in enumerate(self.riwayat, start=1):
            print(f"{i}. {item['jenis']}: Rp{item['jumlah']:,}.")
        print()
        
        
    def __str__(self):
        return f"Pemilik: {self.pemilik}\nSaldo: Rp{self.saldo:,}.\n"
        
        
def main():
    d1 = Dompet("Rafi", 50000)
    d2 = Dompet("Akbar")
    
    d1.setor(50000)
    d2.setor(25000)
    
    d1.tarik(100000)
    d2.tarik(20000)
    
    print(d1)
    print(d2)
    
    d1.lihat_riwayat()
    d2.lihat_riwayat()
    
    
if __name__ == "__main__":
    main()