import streamlit as st

def format_ribuan(nilai):
    return f"{nilai:,.0f}".replace(",", ".")

# TAMBAHAN: logika agar DPP tetap 100% jika nilai ≤ 2 juta
def is_dpp_100persen(nilai):
    return nilai <= 2_000_000

# TAMBAHAN: sesuaikan logika DPP
def calculate_dpp(nilai, kena_ppn):
    if is_dpp_100persen(nilai):
        return nilai
    if kena_ppn:
        return (100 / 111) * nilai
    return nilai

# TAMBAHAN: sesuaikan logika DPP coretax (untuk faktur PPN)
def calculate_dppcoretax(nilai, kena_ppn):
    if is_dpp_100persen(nilai):
        return nilai
    if kena_ppn:
        return (100 / 111) * (11 / 12) * nilai
    return nilai     

def calculate_ppn(dpp):
    return 0.12 * dppcoretax  # Catatan: dppcoretax akan didefinisikan di bawah

def calculate_pph22(dpp):
    return 0.015 * dpp

def calculate_pph23(dpp):
    return 0.02 * dpp

st.title("Kalkulator Pajak dengan DPP")

# Langkah 1: Apakah kena PPN?
kena_ppn = st.radio(":blue[Apakah transaksi dikenakan PPN?]", ["Ya", "Tidak"]) == "Ya"

# Langkah 2: Pilih jenis PPh
jenis_pph = st.selectbox(":blue[Pilih Jenis PPh]", ["PPh 22", "PPh 23"])

# Langkah 3: Input nilai transaksi
nilai_str = st.text_input(":blue[Masukkan Nilai Transaksi (misal: 1.000.000)]")

if nilai_str:
    try:
        nilai = float(nilai_str.replace(".", "").replace(",", "."))

        # Hitung DPP dan DPP untuk PPN coretax
        dpp = calculate_dpp(nilai, kena_ppn)
        dppcoretax = calculate_dppcoretax(nilai, kena_ppn)

        st.write(f"**Nilai Transaksi:** Rp {format_ribuan(nilai)}")                

        # Tampilkan DPP dan PPN hanya jika nilai > 2 juta dan dikenakan PPN
        if kena_ppn and not is_dpp_100persen(nilai):
            ppn = calculate_ppn(dppcoretax)
            st.info(f"**DPP (Dasar Pengenaan Pajak) PPN - Faktur Pajak Coretax =** Rp {format_ribuan(dppcoretax)}")
            st.info(f"**PPN (12%) = Rp {format_ribuan(ppn)}**")          

        # Tampilkan DPP untuk PPh
        st.success(f"**DPP (Dasar Pengenaan Pajak) PPh - e-bupot =** Rp {format_ribuan(dpp)}")        

        # Hitung dan tampilkan PPh
        if jenis_pph == "PPh 22":
            if dpp <= 2_000_000:
                st.info("**PPh 22 tidak dikenakan untuk transaksi ≤ Rp 2.000.000.**")
            else:
                pph22 = calculate_pph22(dpp)
                st.warning(f"**PPh 22 (1,5%) = Rp {format_ribuan(pph22)}**")

        elif jenis_pph == "PPh 23":
            pph23 = calculate_pph23(dpp)
            st.warning(f"**PPh 23 (2%) = Rp {format_ribuan(pph23)}**")

    except ValueError:
        st.error("Masukkan angka yang valid.")
