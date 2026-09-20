import streamlit as st
import pandas as pd
import joblib

# Load model
pipeline = joblib.load('models/kmeans_model.joblib')

st.set_page_config( page_title='Student Performance', page_icon='🧑🏻‍💼', layout='centered' )

st.title('🧑🏻‍💼 Student Performance')

st.write('Masukkan nilai penilaian siswa untuk menghitung ' 'nilai akhir berdasarkan persentase bobot yang tetap.' )

# ==========================================
# THRESHOLD BATAS AMBANG
# ==========================================

THRESHOLD_SANGAT_BAIK = 92.0
THRESHOLD_CUKUP_BAIK = 76.0

# ==========================================
# VALIDASI NILAI AKHIR
# ==========================================

if not 0 <= nilai_akhir <= 100:
    st.error('Nilai akhir berada di luar rentang 0–100.')
    st.stop()

# ==========================================
# KLASIFIKASI BERDASARKAN THRESHOLD
# ==========================================

if nilai_akhir >= THRESHOLD_SANGAT_BAIK:
    kategori = 'Sangat Baik'

    pesan = (
        '📌 Pertahankan konsistensi belajar '
        'dan hasil akademik.'
    )

    jenis_pesan = 'success'

elif nilai_akhir >= THRESHOLD_CUKUP_BAIK:
    kategori = 'Cukup Baik'

    pesan = (
        '📌 Fokus pada penguatan materi yang '
        'belum dikuasai dan jaga konsistensi belajar.'
    )

    jenis_pesan = 'info'

else:
    kategori = 'Perlu Ditingkatkan'

    pesan = (
        '📌 Diperlukan pembelajaran pada topik '
        'yang belum dikuasai, disertai materi '
        'tambahan dan latihan terarah.'
    )

    jenis_pesan = 'warning'

# ==========================================
# TAMPILKAN HASIL KATEGORI
# ==========================================

st.write(f'**Nilai Akhir:** {nilai_akhir:.2f}')
st.write(f'**Kategori:** {kategori}')

if jenis_pesan == 'success':
    st.success(f'Kategori: **{kategori}**')

elif jenis_pesan == 'info':
    st.info(f'Kategori: **{kategori}**')

else:
    st.warning(f'Kategori: **{kategori}**')

st.info(pesan)
