import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np
import io
# layout Streamlit
st.image("https://graduation.president.ac.id/assets/logo.png", width=500)

import streamlit as st
from PIL import Image, ImageEnhance
from io import BytesIO
import streamlit as st
from PIL import Image, ImageEnhance

# Judul aplikasi
st.title("Proyek Manipulasi Gambar")

# Daftar anggota dengan nama, deskripsi, dan path ke foto
anggota = [
    {"nama": "John Doe", "deskripsi": "Anggota bagian pengembangan perangkat lunak.", "foto": "john_doe.jpg"},
    {"nama": "Jane Smith", "deskripsi": "Anggota bagian desain UI/UX.", "foto": "jane_smith.jpg"},
    {"nama": "Michael Johnson", "deskripsi": "Anggota bagian manajemen proyek.", "foto": "michael_johnson.jpg"},
    {"nama": "Emily Davis", "deskripsi": "Anggota bagian pengujian dan QA.", "foto": "emily_davis.jpg"},
]

# Sidebar menu
menu = st.sidebar.radio("Pilih Menu:", ["Nama Anggota", "Isi Website"])

# Menu 1: Nama Anggota
if menu == "Nama Anggota":
    st.header("Daftar Anggota dan Jobdesk")
    for member in anggota:
        # Menampilkan foto anggota
        try:
            foto = Image.open(member["foto"])  # Pastikan file foto tersedia di direktori
            st.image(foto, caption=member["nama"], width=150)
        except FileNotFoundError:
            st.warning(f"Foto untuk {member['nama']} tidak ditemukan.")

        # Menampilkan nama dan deskripsi anggota
        st.subheader(member["nama"])
        st.write(f"**Deskripsi:** {member['deskripsi']}")
        st.markdown("---")  # Garis pemisah antar anggota

# Menu 2: Isi Website
elif menu == "Isi Website":
    st.header("Manipulasi Gambar")
    st.write("Di sini Anda dapat mengunggah gambar dan memanipulasinya.")
    
    # Upload gambar
    uploaded_image = st.file_uploader("Unggah gambar", type=["png", "jpg", "jpeg"])
    if uploaded_image is not None:
        img = Image.open(uploaded_image)
        st.image(img, caption="Gambar yang diunggah", use_column_width=True)

        # Opsi manipulasi gambar
        st.write("### Opsi Manipulasi Gambar:")
        
        # 1. Pengaturan skala
        scale = st.slider("Skala gambar (persentase)", 10, 200, 100)
        scaled_width = int(img.width * scale / 100)
        scaled_height = int(img.height * scale / 100)
        img_scaled = img.resize((scaled_width, scaled_height))
        st.image(img_scaled, caption="Gambar setelah diskalakan", use_column_width=True)

        # 2. Rotasi gambar
        rotation = st.slider("Rotasi gambar (derajat)", 0, 360, 0)
        img_rotated = img_scaled.rotate(rotation)
        st.image(img_rotated, caption="Gambar setelah dirotasi", use_column_width=True)

        # 3. Pengaturan cahaya
        brightness = st.slider("Kecerahan gambar", 0.1, 3.0, 1.0)
        enhancer = ImageEnhance.Brightness(img_rotated)
        img_brightened = enhancer.enhance(brightness)
        st.image(img_brightened, caption="Gambar setelah pengaturan cahaya", use_column_width=True)

        # Fitur download gambar
        st.write("### Unduh Gambar")
        format_options = st.radio("Pilih format file:", ["PNG", "JPG", "PDF"])

        # Menyimpan gambar ke buffer
        from io import BytesIO
        img_buffer = BytesIO()
        if format_options == "PNG":
            img_brightened.save(img_buffer, format="PNG")
            file_ext = "png"
        elif format_options == "JPG":
            img_brightened.save(img_buffer, format="JPEG")
            file_ext = "jpg"
        elif format_options == "PDF":
            img_brightened.save(img_buffer, format="PDF")
            file_ext = "pdf"

        # Membuat tombol unduh
        st.download_button(
            label=f"Unduh Gambar ({file_ext.upper()})",
            data=img_buffer.getvalue(),
            file_name=f"hasil_gambar.{file_ext}",
            mime=f"image/{file_ext}" if file_ext != "pdf" else "application/pdf"
        )
