import requests
import json
import csv
from tabulate import tabulate

url = "https://jsonplaceholder.typicode.com/posts"
FILE_JSON = "posts.json"
FILE_CSV = "posts.csv"


def ambil_data():
    try:
        resp = requests.get(url, params={"_limit": 10}, timeout=10)
        resp.raise_for_status()
        data = resp.json()
    except requests.exceptions.RequestException as e:
        print(f"\nGagal mengambil data: {e}\n")
        return []
    
    return data
    
    
def cetak_tabel(data):
    data_baru = [
        {
            "id": item["id"],
            "title": item["title"][:40]
        } 
        for item in data
    ]
    
    tabel = tabulate(
        data_baru,
        headers="keys",
        tablefmt="grid"
    )
    
    print(f"\n{tabel}\n")


def simpan_data(data):
    with open(FILE_JSON, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
        
    print(f"Data berhasil disimpan ke '{FILE_JSON}' ✓\n")


def ekspor_csv(data):
    header = []
    for item in data:
        for key in item:
            if key not in header:
                header.append(key)
    
    with open(FILE_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=header)
        writer.writeheader()
        writer.writerows(data)
        
    print(f"Data berhasil diekspor ke '{FILE_CSV}'' ✓\n")


def main():
    data = ambil_data()
    if not data:
        return 
    
    cetak_tabel(data)
    simpan_data(data)
    ekspor_csv(data)
    
    
if __name__ == "__main__":
    main()