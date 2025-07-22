import streamlit as st

def format_ribuan(nilai):
    return f"{nilai:,.0f}".replace(",", ".")

def calculate_pph22(amount):
    return 0.015 * amount

def calculate_pph23(amount):
    return 0.02 * amount

def calculate_ppn(amount):
    return 0.11 * amount

st.title("Kalkulator Pajak Sederhana")

# Pilihan jenis pajak
jenis_pajak = st.selectbox("Pilih Jenis Pajak", ["PPh 22", "PPh 23", "PPN"])

# Input nilai transaksi (pakai text_input agar bisa masukkan format ribuan)
nilai_str = st.text_input("Masukkan Nilai Transaksi (misal: 1.000.000)")

if nilai_str:
    try:
        nilai = float(nilai_str.replace(".", "").replace(",", "."))
        st.write(f"**Nilai Transaksi:** Rp {format_ribuan(nilai)}")

        # Tampilkan hanya pajak yang dipilih
        if jenis_pajak == "PPh 22":
            pph22 = calculate_pph22(nilai)
            st.write(f"**PPh 22 (1,5%) = Rp {format_ribuan(pph22)}**")

        elif jenis_pajak == "PPh 23":
            pph23 = calculate_pph23(nilai)
            st.write(f"**PPh 23 (2%) = Rp {format_ribuan(pph23)}**")

        elif jenis_pajak == "PPN":
            ppn = calculate_ppn(nilai)
            st.write(f"**PPN (11%) = Rp {format_ribuan(ppn)}**")

    except ValueError:
        st.error("Masukkan angka yang valid.")
