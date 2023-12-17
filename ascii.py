import streamlit as st

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

def string_to_bin(input):
    return ''.join(format(ord(i), '08b') for i in input)

def main():
    st.title("String to Binary Converter")

    # Meminta input dari pengguna untuk plaintext (kunci)
    plaintext = st.text_input("Masukkan plaintext (kunci):")

    # Meminta input dari pengguna menggunakan text_area agar dapat memasukkan beberapa string sekaligus
    my_strings = st.text_area("Masukkan beberapa string (pisahkan dengan baris):")

    if my_strings and plaintext:
        # Mengubah plaintext menjadi representasi biner kunci
        key_bin_string = string_to_bin(plaintext)

        # Memisahkan string biner kunci menjadi blok 8 bit
        key_bin_chunks = list(chunks(key_bin_string, 8))

        # Membagi string menjadi list berdasarkan baris
        strings_list = my_strings.split('\n')

        # Mencetak blok 8 bit untuk kunci
        st.write("Hasil untuk Kunci:")
        for chunk in key_bin_chunks:
            st.write(chunk)

        # Mencetak blok 8 bit untuk setiap string
        st.write("Hasil untuk Setiap String:")
        for my_string in strings_list:
            # Mengubah string menjadi representasi biner
            bin_string = string_to_bin(my_string)

            # Memisahkan string biner menjadi blok 8 bit
            bin_chunks = list(chunks(bin_string, 8))

            # Mencetak blok 8 bit untuk setiap string
            st.write(bin_chunks)

if __name__ == "__main__":
    main()
