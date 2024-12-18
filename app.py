"""
    140810220002 - Muhammad Faiz Fahri
    140810200041 - Mohammad Aria Ardhana
    140810220080 - Muhammad Satria Dharma
"""

import streamlit as st
import math

st.markdown("""
<style>
[data-testid="stMain"] {
    background-image: url("https://static.vecteezy.com/system/resources/previews/008/311/935/non_2x/the-illustration-graphic-consists-of-abstract-background-with-a-blue-gradient-dynamic-shapes-composition-eps10-perfect-for-presentation-background-website-landing-page-wallpaper-vector.jpg");
    background-size: cover;
}
            
[data-testid="stMain"]::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.7);
}
            
h1, h2, h3, p {
    color: #fff;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("Selamat Datang di Aplikasi Spiral Cipher dan Shift Cipher")
st.sidebar.markdown("---")
st.sidebar.write("""
Aplikasi ini dibuat untuk mengenkripsi maupun men-dekripsi file .txt anda menggunakan spiral cipher maupun shift cipher 

140810220002 - Muhammad Faiz Fahri
140810200041 - Mohammad Aria Ardhana
140810220080 - Muhammad Satria Dharma
""")

# Fungsi untuk enkripsi dan dekripsi Shift Cipher
def shift_cipher(text, shift, mode='encrypt'):
    result = []
    for char in text:
        if char.isalpha():
            offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - offset + (shift if mode == 'encrypt' else -shift)) % 26 + offset)
            result.append(shifted_char)
        else:
            result.append(char)  # Non-alphabet characters tidak diubah
    return ''.join(result)

# Fungsi untuk menentukan ukuran matriks ganjil berdasarkan panjang teks
def orde(text):
    panjang = len(text)
    ukuran = math.ceil(math.sqrt(panjang))
    if ukuran % 2 == 0:
        ukuran += 1  # Pastikan ukuran matriks ganjil
    return ukuran

# Fungsi untuk menghitung panjang padding yang diperlukan
def cek(text):
    i = orde(text)
    return (i * i) - len(text)

# Fungsi untuk menambahkan padding ('x') pada teks
def encrypt_padding(teks, kurang):
    return teks + 'x' * kurang

# Fungsi untuk mengenkripsi teks dalam bentuk spiral
def spiral_encrypt(arr):
    O = orde(arr)
    padding_length = cek(arr)
    padded_text = encrypt_padding(arr, padding_length)

    # Membuat matriks untuk enkripsi spiral
    matrix = [[None] * O for _ in range(O)]
    top, bottom, left, right = 0, O - 1, 0, O - 1
    index = 0

    while True:
        if left > right:
            break

        # Isi baris atas dari kiri ke kanan
        for i in range(left, right + 1):
            matrix[top][i] = padded_text[index]
            index += 1
        top += 1

        if top > bottom:
            break

        # Isi kolom kanan dari atas ke bawah
        for i in range(top, bottom + 1):
            matrix[i][right] = padded_text[index]
            index += 1
        right -= 1

        if left > right:
            break

        # Isi baris bawah dari kanan ke kiri
        for i in range(right, left - 1, -1):
            matrix[bottom][i] = padded_text[index]
            index += 1
        bottom -= 1

        if top > bottom:
            break

        # Isi kolom kiri dari bawah ke atas
        for i in range(bottom, top - 1, -1):
            matrix[i][left] = padded_text[index]
            index += 1
        left += 1

    # Gabungkan hasil spiral menjadi satu string
    result = ''.join(''.join(row) for row in matrix)
    return result

# Fungsi untuk dekripsi spiral cipher
def spiral_decrypt(input_str):
    n = int(math.sqrt(len(input_str)))
    matrix = [[None] * n for _ in range(n)]

    index = 0
    for i in range(n):
        for j in range(n):
            matrix[i][j] = input_str[index]
            index += 1

    result = ""
    top, bottom, left, right = 0, n - 1, 0, n - 1

    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result += matrix[top][i]
        top += 1

        for i in range(top, bottom + 1):
            result += matrix[i][right]
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result += matrix[bottom][i]
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result += matrix[i][left]
            left += 1

    return result

# Streamlit App with Tabs
st.title("Aplikasi Enkripsi dan Dekripsi")

tab1, tab2, tab3, tab4 = st.tabs([
    "Shift Cipher (Manual Input)",
    "Shift Cipher (File Upload)",
    "Spiral Cipher (Manual Input)",
    "Spiral Cipher (File Upload)"
])

# --- Tab 1: Shift Cipher (Manual Input) ---
with tab1:
    st.header("Shift Cipher (Manual Input)")

    mode = st.radio("Pilih Mode", ('Enkripsi', 'Dekripsi'), key="shift_cipher_mode1")
    shift = st.number_input("Masukkan Nilai Shift", min_value=1, max_value=25, value=3, key="shift_value1")
    text_input = st.text_area("Masukkan Teks", "", key="text_input1")

    if st.button("Proses", key="process_shift_cipher1"):
        if mode == 'Enkripsi':
            result = shift_cipher(text_input, shift, mode='encrypt')
        else:
            result = shift_cipher(text_input, shift, mode='decrypt')
        st.text_area("Hasil", result, height=200, key="result_shift_cipher1")
        st.download_button(label="Download Hasil", data=result, file_name="shift_cipher_result.txt", mime="text/plain", key="download_shift_cipher1")

# --- Tab 2: Shift Cipher (File Upload) ---
with tab2:
    st.header("Shift Cipher (File Upload)")

    mode = st.radio("Pilih Mode", ('Enkripsi', 'Dekripsi'), key="shift_cipher_mode2")
    shift = st.number_input("Masukkan Nilai Shift", min_value=1, max_value=25, value=3, key="shift_value2")

    uploaded_file = st.file_uploader("Pilih File .txt", type=["txt"], key="file_upload_shift_cipher")

    if uploaded_file is not None:
        file_content = uploaded_file.read().decode("utf-8")

        if st.button("Proses File", key="process_file_shift_cipher"):
            if mode == 'Enkripsi':
                result = shift_cipher(file_content, shift, mode='encrypt')
            else:
                result = shift_cipher(file_content, shift, mode='decrypt')

            st.text_area("Hasil", result, height=200, key="result_file_shift_cipher")
            st.download_button(label="Download Hasil", data=result, file_name="shift_cipher_result.txt", mime="text/plain", key="download_shift_cipher2")

# --- Tab 3: Spiral Cipher (Manual Input) ---
with tab3:
    st.header("Spiral Cipher (Manual Input)")

    mode = st.radio("Pilih Mode", ('Enkripsi', 'Dekripsi'), key="spiral_cipher_mode1")
    text_input = st.text_area("Masukkan Teks", "", key="text_input_spiral1")

    if st.button("Proses", key="process_spiral_cipher1"):
        if mode == 'Enkripsi':
            result = spiral_encrypt(text_input)
        else:
            result = spiral_decrypt(text_input)
        st.text_area("Hasil", result, height=200, key="result_spiral_cipher1")
        st.download_button(label="Download Hasil", data=result, file_name="spiral_cipher_result.txt", mime="text/plain", key="download_spiral_cipher1")

# --- Tab 4: Spiral Cipher (File Upload) ---
with tab4:
    st.header("Spiral Cipher (File Upload)")

    mode = st.radio("Pilih Mode", ('Enkripsi', 'Dekripsi'), key="spiral_cipher_mode2")
    uploaded_file = st.file_uploader("Pilih File .txt", type=["txt"], key="file_upload_spiral_cipher")

    if uploaded_file is not None:
        file_content = uploaded_file.read().decode("utf-8")

        if st.button("Proses File", key="process_file_spiral_cipher"):
            if mode == 'Enkripsi':
                result = spiral_encrypt(file_content)
            else:
                result = spiral_decrypt(file_content)

            st.text_area("Hasil", result, height=200, key="result_file_spiral_cipher")
            st.download_button(label="Download Hasil", data=result, file_name="spiral_cipher_result.txt", mime="text/plain", key="download_spiral_cipher2")