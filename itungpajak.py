import streamlit as st

def format_ribuan(nilai):
    return f"{nilai:,.0f}".replace(",", ".")

def calculate_dpp(nilai, kena_ppn):
    if kena_ppn:
        return (100 / 111) * nilai
    return nilai

def calculate_ppn(dpp):
    return 0.11 * dpp

def calculate_pph22(dpp):
    return 0.015 * dpp

def calculate_pph23(dpp):
    return 0.02 * dpp

def calculate_pph4a2(dpp):
    return 0.0175 * dpp

st.info("""
# Aplikasi Hitung Pajak
Ini adalah aplikasi untuk menghitung pajak secara online
""")



# Langkah 1: Apakah kena PPN?
kena_ppn = st.radio(":blue[Apakah transaksi dikenakan PPN?]", ["Ya", "Tidak"]) == "Ya"

# Langkah 2: Pilih jenis PPh
jenis_pph = st.selectbox(":blue[Pilih Jenis PPh]", ["Pilih Jenis PPh", "PPh 22", "PPh 23", "PPh 4 Ayat 2"])

# Langkah 3: Input nilai transaksi
nilai_str = st.text_input(":blue[Masukkan Nilai Transaksi (misal: 1.000.000)]")

if nilai_str:
    try:
        nilai = float(nilai_str.replace(".", "").replace(",", "."))
        dpp = calculate_dpp(nilai, kena_ppn)

        st.write(f"**Nilai Transaksi:** Rp {format_ribuan(nilai)}")
        st.write(f"**DPP (Dasar Pengenaan Pajak):** Rp {format_ribuan(dpp)}")

        if kena_ppn:
            ppn = calculate_ppn(dpp)
            st.info(f"**PPN (11%) = Rp {format_ribuan(ppn)}**")

        if jenis_pph == "PPh 22":
            pph22 = calculate_pph22(dpp)
            st.info(f"**PPh 22 (1,5%) = Rp {format_ribuan(pph22)}**")
        elif jenis_pph == "PPh 23":
            pph23 = calculate_pph23(dpp)
            st.info(f"**PPh 23 (2%) = Rp {format_ribuan(pph23)}**")
        elif jenis_pph == "PPh 4 Ayat 2":
            pph4a2 = calculate_pph4a2(dpp)
            st.info(f"**PPh 4 Ayat 2 (1,75%) = Rp {format_ribuan(pph4a2)}**")

    except ValueError:
        st.error("Masukkan angka yang valid.")
