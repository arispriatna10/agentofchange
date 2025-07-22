import streamlit as st

def format_ribuan(nilai):
    return f"{nilai:,.0f}".replace(",", ".")

def calculate_pph22(amount):
    return 0.015 * amount

def calculate_pph23(amount):
    return 0.02 * amount

def calculate_ppn(amount):
    return 0.11 * amount

st.title("Kalkulator Pajak: PPN & PPh 22/23")

# Langkah 1: Pilih apakah pakai PPN
pakai_ppn = st.radio("Apakah transaksi dikenakan PPN?", ["Ya", "Tidak"])

# Langkah 2: Pilih jenis PPh
jenis_pph = st.selectbox("Pilih Jenis PPh", ["PPh 22", "PPh 23"])

# Langkah 3: Input nilai transaksi
nilai_str = st.text_input("Masukkan Nilai Transaksi (misal: 1.000.000)")

if nilai_str:
    try:
        nilai = float(nilai_str.replace(".", "").replace(",", "."))
        st.write(f"**Nilai Transaksi:** Rp {format_ribuan(nilai)}")

        # Hitung dan tampilkan pajak sesuai pilihan
        if pakai_ppn == "Ya":
            ppn = calculate_ppn(nilai)
            st.write(f"**PPN (11%) = Rp {format_ribuan(ppn)}**")

        if jenis_pph == "PPh 22":
            pph22 = calculate_pph22(nilai)
            st.write(f"**PPh 22 (1,5%) = Rp {format_ribuan(pph22)}**")
        elif jenis_pph == "PPh 23":
            pph23 = calculate_pph23(nilai)
            st.write(f"**PPh 23 (2%) = Rp {format_ribuan(pph23)}**")

    except ValueError:
        st.error("Masukkan angka yang valid.")
