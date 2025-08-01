import streamlit as st

def format_ribuan(nilai):
    return f"{nilai:,.0f}".replace(",", ".")

def calculate_dpp(nilai, kena_ppn):
    # Jika transaksi kecil, DPP = nilai 100%
    if nilai <= 2000000:
        return nilai
    # Jika kena PPN, gunakan rumus 100/111
    if kena_ppn:
        return (100 / 111) * nilai
    return nilai

def calculate_dppcoretax(nilai, kena_ppn):
    # Jika transaksi kecil, DPP = nilai 100%
    if nilai <= 2000000:
        return nilai
    # Jika kena PPN, gunakan rumus (100 / 111) * (11 / 12)
    if kena_ppn:
        return (100 / 111) * (11 / 12) * nilai
    return nilai     

def calculate_ppn(dppcoretax):
    return 0.12 * dppcoretax

def calculate_pph22(dpp):
    return 0.015 * dpp

def calculate_pph23(dpp):
    return 0.02 * dpp

st.title("Kalkulator Pajak dengan DPP")

kena_ppn = st.radio(":blue[Apakah transaksi dikenakan PPN?]", ["Ya", "Tidak"]) == "Ya"
jenis_pph = st.selectbox(":blue[Pilih Jenis PPh]", ["PPh 22", "PPh 23"])
nilai_str = st.text_input(":blue[Masukkan Nilai Transaksi (misal: 1.000.000)]")

if nilai_str:
    try:
        nilai = float(nilai_str.replace(".", "").replace(",", "."))

        # Perhitungan DPP utama dan DPP untuk coretax
        dpp = calculate_dpp(nilai, kena_ppn)
        dppcoretax = calculate_dppcoretax(nilai, kena_ppn)

        st.write(f"**Nilai Transaksi:** Rp {format_ribuan(nilai)}")

        # Tampilkan DPP dan PPN hanya jika transaksi > 2 juta
        if kena_ppn and dpp > 2000000:
            ppn = calculate_ppn(dppcoretax)
            st.info(f"**DPP (Dasar Pengenaan Pajak) PPN - Faktur Pajak Coretax =** Rp {format_ribuan(dppcoretax)}")
            st.info(f"**PPN (12%) = Rp {format_ribuan(ppn)}**")    
        elif kena_ppn and dpp <= 2000000:
            st.info("PPN tidak dikenakan untuk transaksi ≤ Rp 2.000.000.")

        # Perhitungan PPh 22 dan 23
        if jenis_pph == "PPh 22":
            if dpp > 2000000:
                st.success(f"**DPP (Dasar Pengenaan Pajak) PPh - e-bupot =** Rp {format_ribuan(dpp)}") 
                pph22 = calculate_pph22(dpp)
                st.warning(f"**PPh 22 (1,5%) = Rp {format_ribuan(pph22)}**")
            else:
                st.info("PPh 22 tidak dikenakan untuk transaksi ≤ Rp 2.000.000.")
        elif jenis_pph == "PPh 23":
            st.success(f"**DPP (Dasar Pengenaan Pajak) PPh - e-bupot =** Rp {format_ribuan(dpp)}") 
            pph23 = calculate_pph23(dpp)
            st.warning(f"**PPh 23 (2%) = Rp {format_ribuan(pph23)}**")

    except ValueError:
        st.error("Masukkan angka yang valid.")
