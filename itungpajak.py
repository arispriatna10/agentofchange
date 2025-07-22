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

st.title("🧾 Kalkulator Pajak")

# Input area
kena_ppn = st.radio("Apakah transaksi dikenakan PPN?", ["Ya", "Tidak"]) == "Ya"
jenis_pph = st.selectbox("Pilih Jenis PPh", ["PPh 22", "PPh 23", "Tidak Ada"])
nilai_str = st.text_input("Masukkan Nilai Transaksi (misal: 1.000.000)")

# Tombol eksekusi
if st.button("Hitung Pajak"):
    if nilai_str:
        try:
            nilai = float(nilai_str.replace(".", "").replace(",", "."))
            dpp = calculate_dpp(nilai, kena_ppn)

            st.markdown(f"**📌 Nilai Transaksi:** Rp {format_ribuan(nilai)}")
            st.markdown(f"**📌 DPP (Dasar Pengenaan Pajak):** Rp {format_ribuan(dpp)}")

            total_pajak = 0

            if kena_ppn:
                ppn = calculate_ppn(dpp)
                total_pajak += ppn
                st.markdown(f"🟡 **PPN (11%) = Rp {format_ribuan(ppn)}**")

            if jenis_pph == "PPh 22":
                pph22 = calculate_pph22(dpp)
                total_pajak += pph22
                st.markdown(f"🟢 **PPh 22 (1,5%) = Rp {format_ribuan(pph22)}**")
            elif jenis_pph == "PPh 23":
                pph23 = calculate_pph23(dpp)
                total_pajak += pph23
                st.markdown(f"🟢 **PPh 23 (2%) = Rp {format_ribuan(pph23)}**")

            st.divider()
            st.markdown(f"🧮 **Total Pajak: Rp {format_ribuan(total_pajak)}**")
            st.markdown(f"💰 **Nilai Setelah Pajak: Rp {format_ribuan(nilai - total_pajak)}**")

        except ValueError:
            st.error("Masukkan angka transaksi yang valid.")
    else:
        st.warning("Masukkan nilai transaksi terlebih dahulu.")
