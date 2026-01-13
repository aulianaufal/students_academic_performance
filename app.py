import streamlit as st
import pandas as pd
import joblib

# Load model
pipeline = joblib.load('models/kmeans_model.joblib')

st.title('🧑🏻‍💼Student Performance')

st.write('Masukkan nilai akademik siswa untuk menentukan hasil performa.')

# Input numerik
math = st.number_input('Math Score', min_value=0)
reading = st.number_input('Reading Score', min_value=0, max_value=100)
writing = st.number_input('Writing Score', min_value=0, max_value=100)

if st.button('Result'):
    # Validasi saat submit
    if math == 0 or reading == 0 or writing == 0:
        st.error('Nilai belum lengkap. Mohon lengkapi semua nilai sebelum melihat hasil.')
        st.stop()

    # DataFrame sesuai dengan fitur saat training
    input_df = pd.DataFrame([{
        'math score': math,
        'reading score': reading,
        'writing score': writing
    }])

    # Kolom skor rata-rata (merge scores)
    input_df['score'] = input_df[['math score', 'reading score', 'writing score']].mean(axis=1)

    # Thresholds bisa diubah sesuai kebutuhan
    PERTAHANKAN_THRESHOLD = 92  # >= -> Sangat Baik
    CUKUP_THRESHOLD = 76        # >=CUKUP_THRESHOLD and < PERTAHANKAN_THRESHOLD -> Cukup Baik

    avg = input_df['score'].iloc[0]
    if avg >= PERTAHANKAN_THRESHOLD:
        st.success(f'Rata-rata nilai: {avg:.2f}. Siswa termasuk kategori **Sangat Baik**.')
        st.info('📌 Pertahankan konsistensi belajar.')
    elif avg >= CUKUP_THRESHOLD:
        st.info(f'Rata-rata nilai: {avg:.2f}. Siswa termasuk kategori **Cukup Baik**.')
        st.info('📌 Fokus pada penguatan materi yang belum dikuasai dan jaga konsistensi belajar.')
    else:
        st.warning(f'Rata-rata nilai: {avg:.2f}. Siswa termasuk kategori **Perlu Ditingkatkan**.')

        st.info('📌 Berdasarkan hasil evaluasi, diperlukan pembelajaran pada topik yang belum dikuasai, disertai materi tambahan dan latihan terarah untuk meningkatkan pemahaman materi.')
