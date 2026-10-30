
import pandas as pd
from pathlib import Path

# Membaca semua file CSV di folder ini
folder = Path(__file__).parent

for file in sorted(folder.glob("*.csv")):
    print("\n" + "=" * 50)
    print("FILE:", file.name)

    df = pd.read_csv(file)

    print("Jumlah baris:", len(df))
    print("Kolom:", list(df.columns))

    if "tanggal" in df.columns:
        df["tanggal"] = pd.to_datetime(df["tanggal"], errors="coerce")
        print("\nJumlah baris per tahun:")
        print(df["tanggal"].dt.year.value_counts().sort_index().to_string())

    print("\nJumlah nilai kosong per kolom:")
    print(df.isna().sum().to_string())

    if "tanggal" in df.columns and "stasiun" in df.columns:
        duplikat = df.duplicated(
            subset=["tanggal", "stasiun"]
        ).sum()
        print("\nDuplikasi tanggal + stasiun:", duplikat)
