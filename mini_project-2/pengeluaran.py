import json
import csv
from datetime import date
from tabulate import tabulate

FILE_JSON = "pengeluaran.json"
FILE_CSV = "pengeluaran.csv"


def simpan_data(data):
    with open(FILE_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def muat_data():
    try:
        with open(FILE_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("File data rusak, mulai dari data kosong.\n")
        return []
    
    if not isinstance(data, list):
        print("Format data salah, mulai dari data kosong.\n")
        return []
        
    return data


def tambah_pengeluaran():
    while True:
        try:
            kategori = input("Kategori: ").strip()
        except KeyboardInterrupt:
            print("Input dibatalkan...\n")
            return
        
        if not kategori:
            print("Kategori tidak boleh kosong!\n")
            continue
        
        break
    
    while True:
        try:
            jumlah = int(input("Jumlah: Rp").replace(".", "").replace(",", ""))
        except ValueError:
            print("Harap masukkan angka!\n")
            continue
        except KeyboardInterrupt:
            print("Input dibatalkan...\n")
            return
            
        if jumlah <= 0:
            print("Jumlah harus di atas 0!\n")
            continue
        
        break
    
    while True:
        try:
            keterangan = input("Keterangan: ").strip()
        except KeyboardInterrupt:
            print("Input dibatalkan...\n")
            return
        
        if not keterangan:
            print("Keterangan tidak boleh kosong!\n")
            continue
        
        break
    
    data_baru = {
        "tanggal": date.today().isoformat(),
        "kategori": kategori,
        "jumlah": jumlah,
        "keterangan": keterangan
    }
    
    data = muat_data()
    data.append(data_baru)
    simpan_data(data)
    print(f"Berhasil menambahkan {keterangan} ✓\n")


def lihat_pengeluaran():
    data = muat_data()
    if not data:
        print("Belum ada pengeluaran!\n")
        return
    
    tabel = tabulate(
        data,
        headers="keys",
        tablefmt="simple",
        showindex=range(1, len(data) + 1),
        intfmt=","
    )
    
    print(f"\n{tabel}\n")
    total = sum(item['jumlah'] for item in data)
    print(f"Total: Rp{total:,}\n")
    
    
def ekspor_csv():
    data = muat_data()
    header = ["tanggal", "kategori", "jumlah", "keterangan"]
    
    if not data:
        print("Belum ada pengeluaran!\n")
        return
    
    with open(FILE_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)
        
    print("Berhasil mengekspor data ke CSV ✓\n")
    
            
def main():
    while True:
        print("=== Catatan Pengeluaran CLI ===")
        print("1. Tambah Pengeluaran")
        print("2. Lihat Pengeluaran")
        print("3. Ekspor CSV")
        print("4. Keluar\n")
        
        try:
            pilihan = input("Masukkan pilihan (1/2/3/4): ")
        except KeyboardInterrupt:
            print("Program dihentikan...\n")
            return
        
        if pilihan == "1":
            tambah_pengeluaran()
        elif pilihan == "2":
            lihat_pengeluaran()
        elif pilihan == "3":
            ekspor_csv()
        elif pilihan == "4":
            print("Terima kasih!\n")
            return
        else:
            print("Pilihan tidak tersedia!\n")
    
    
if __name__ == "__main__":
    main()