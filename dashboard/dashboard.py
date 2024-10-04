import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

st.title('Analisis Bike Sharing')
st.write("Ini adalah dashboard sederhana yang menampilkan hasil analisis dataset.")

days = pd.read_csv('..\data\days.csv')
hour = pd.read_csv('..\data\hours.csv')

st.write("Data days")
st.dataframe(days.head())  # Menampilkan 5 data teratas dari data days
st.write("Data hour")
st.dataframe(hour.head())  # Menampilkan 5 data teratas dari data hour

st.subheader('Grafik Rata-Rata Penyewaan per Musim')
import streamlit as st
import matplotlib.pyplot as plt

# Data musim dan penyewaan
musim = ['Gugur', 'Panas', 'Dingin', 'Semi']
count_cr_days = [5644.30, 4992.33, 4728.16, 2604.13]  # Data dari DataFrame days
count_cr_hour = [236.02, 208.34, 198.87, 111.11]  # Data dari DataFrame hour


# Membuat figure dan axis untuk bar chart
fig, ax = plt.subplots(figsize=(10, 6))

# Membuat bar chart untuk data days
ax.bar(musim, count_cr_days, width=0.4, label='Days', align='center', color='skyblue')

# Membuat bar chart untuk data hour
ax.bar(musim, count_cr_hour, width=0.4, label='Hour', align='edge', color='lightgreen')

# Menambahkan label, judul, dan legend
ax.set_xlabel('Musim')
ax.set_ylabel('Rata-Rata Penyewaan')
ax.set_title('Rata-Rata Penyewaan per Musim')
ax.legend()

# Menampilkan grafik di Streamlit
st.pyplot(fig)
st.write("""
Dapat dilihat bahwa Musim gugur secara konsisten menunjukkan rata-rata penyewaan tertinggi di kedua data, baik berdasarkan data harian maupun per jam.

- **Musim Gugur**: 5,644.30 (days), 236.02 (hour)
- **Musim Panas**: 4,992.33 (days), 208.34 (hour)
- **Musim Dingin**: 4,728.16 (days), 198.87 (hour)
- **Musim Semi**: 2,604.13 (days), 111.11 (hour)
""")


st.subheader('Total Penyewaan Bike Share per Musim')
pb = {'musim': ['Gugur', 'Panas', 'Dingin', 'Semi'],
      'count_cr': [1061129, 918589, 841613, 471348]}  # Data dari kedua DataFrame

# Membuat DataFrame
df = pd.DataFrame(pb)

# Membuat visualisasi bar chart
fig, ax = plt.subplots(figsize=(10, 6))
ax.bar(df['musim'], df['count_cr'], color='purple')
ax.set_xlabel('Musim', fontsize=12)
ax.set_ylabel('Total Penyewaan', fontsize=12)
ax.set_title('Total Penyewaan Bike Share per Musim', fontsize=16)
plt.xticks(rotation=45)  # Memutar label x-axis agar lebih mudah dibaca
ax.grid(axis='y')

# Menampilkan visualisasi di Streamlit
st.pyplot(fig)
st.write("Di sini terlihat dengan jelas bahwa tingkat tertinggi penyewaan bike share berada di musim gugur dengan total penyewaan mencapai 1.061.129 baik untuk data harian maupun per jam.")


st.subheader('Conclusion')
st.write("""
Rata-rata penyewaan di setiap musim mencerminkan preferensi pengguna terhadap layanan bike share, yang mungkin dipengaruhi oleh faktor cuaca, aktivitas luar ruangan, dan acara khusus yang terjadi pada setiap musim. 

Dengan pemahaman ini, pihak penyedia layanan dapat merencanakan strategi yang lebih baik dalam meningkatkan penggunaan bike share di musim-musim yang memiliki tingkat penyewaan lebih rendah. 

Melihat dari berbagai faktor ini, strategi ini bisa menjadi acuan untuk meningkatkan penyewaan bike share di setiap musimnya.
""")

st.write("""
Musim gugur menunjukkan tingkat penyewaan tertinggi dengan total mencapai 1.061.129 unit, diikuti oleh musim panas dengan 918.589 unit, musim dingin dengan 841.613 unit, dan terakhir musim semi dengan 471.348 unit. 

Tentu hal ini bisa didukung oleh banyak faktor menarik yang membuat musim gugur menjadi yang tertinggi, misalnya:
- Cuaca yang menyenangkan
- Acara atau festival yang diadakan di musim gugur
- Pemandangan yang menarik di musim gugur

Semua faktor tersebut membuat musim gugur menjadi yang tertinggi dalam penyewaan dibanding musim lainnya.
""")
