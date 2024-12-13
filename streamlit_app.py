import streamlit as st
from PIL import Image, ImageEnhance
import numpy as np
import io
# layout Streamlit
st.image("https://graduation.president.ac.id/assets/logo.png", width=500)
st.title("PICTIFY")
st.write("by 4 brother")

# Instruksi
st.write("Upload an image and use the following editing features: Scaling, Shear, Brightness Adjustment, and Rotation.")

# Mengunggah gambar
uploaded_file = st.file_uploader("Upload an image (JPG, JPEG, PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Membaca file gambar
    img = Image.open(uploaded_file)

    # Menampilkan gambar asli
    st.subheader("Original Image")
    st.image(img, caption="Original Image", use_column_width=True)

    # Scaling
    st.subheader("Scaling")
    scaling_factor = st.slider("Scaling Factor", 0.1, 5.0, 1.0, 0.1)
    scaled_width = int(img.width * scaling_factor)
    scaled_height = int(img.height * scaling_factor)
    img_scaled = img.resize((scaled_width, scaled_height), Image.Resampling.LANCZOS)

    st.image(img_scaled, caption=f"Scaled Image (Factor: {scaling_factor})", use_column_width=True)

    # Shear
    st.subheader("Shear")
    shear_factor = st.slider("Shear Factor", -1.0, 1.0, 0.0, 0.1)
    img_sheared = img_scaled.transform(
        img_scaled.size,
        Image.AFFINE,
        (1, shear_factor, 0, shear_factor, 1, 0),
        resample=Image.Resampling.BILINEAR,  # Menggunakan BILINEAR
    )
    st.image(img_sheared, caption=f"Sheared Image (Factor: {shear_factor})", use_column_width=True)

    # Brightness Adjustment
    st.subheader("Brightness Adjustment")
    brightness_factor = st.slider("Brightness Factor", 0.1, 3.0, 1.0, 0.1)
    enhancer = ImageEnhance.Brightness(img_sheared)
    img_brightness = enhancer.enhance(brightness_factor)
    st.image(img_brightness, caption=f"Brightness Adjusted (Factor: {brightness_factor})", use_column_width=True)

    # Rotation
    st.subheader("Rotation")
    rotation_angle = st.slider("Rotation Angle (in degrees)", 0, 360, 0, 1)
    img_rotated = img_brightness.rotate(rotation_angle, expand=True)
    st.image(img_rotated, caption=f"Rotated Image ({rotation_angle}°)", use_column_width=True)

    # Download Section
    st.subheader("Download Edited Image")
    format_option = st.radio("Choose the file format:", ["PNG", "JPG", "PDF"])

    # Menyimpan file hasil edit ke buffer
    buffer = io.BytesIO()
    if format_option == "PNG":
        img_rotated.save(buffer, format="PNG")
        mime_type = "image/png"
        file_name = "edited_image.png"
    elif format_option == "JPG":
        img_rotated.convert("RGB").save(buffer, format="JPEG")
        mime_type = "image/jpeg"
        file_name = "edited_image.jpg"
    elif format_option == "PDF":
        img_rotated.convert("RGB").save(buffer, format="PDF")
        mime_type = "application/pdf"
        file_name = "edited_image.pdf"

    # Menampilkan tombol unduh
    st.download_button(
        label=f"Download as {format_option}",
        data=buffer.getvalue(),
        file_name=file_name,
        mime=mime_type,
    )
    import streamlit as st
    import streamlit as st
import streamlit as st
import streamlit as st
import streamlit as st

# Judul aplikasi
st.title("Proyek Manipulasi Gambar")

# Daftar anggota
anggota = [
    {"nama": "John Doe", "deskripsi": "Anggota bagian pengembangan perangkat lunak."},
    {"nama": "Jane Smith", "deskripsi": "Anggota bagian desain UI/UX."},
    {"nama": "Michael Johnson", "deskripsi": "Anggota bagian manajemen proyek."},
    {"nama": "Emily Davis", "deskripsi": "Anggota bagian pengujian dan QA."},
]

# Sidebar menu
menu = st.sidebar.radio("Pilih Menu:", ["Nama Anggota", "Isi Website"])

# Menu 1: Nama Anggota
if menu == "Nama Anggota":
    st.header("Daftar Anggota dan Jobdesk")
    for member in anggota:
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
        from PIL import Image, ImageEnhance
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
