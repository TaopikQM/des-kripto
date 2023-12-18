import streamlit as st

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

def string_to_bin(input):
    return ''.join(format(ord(i), '08b') for i in input)

def main():
    st.title("String to Binary Converter")

    # Meminta input dari pengguna untuk KEY
    key = st.text_input("Masukkan KEY Anda:")

    if key:
        # Mengubah KEY menjadi representasi biner
        bin_key = string_to_bin(key)

        # Memisahkan string biner KEY menjadi blok 8 bit
        bin_chunks_key = list(chunks(bin_key, 8))

        # Mencetak blok 8 bit untuk KEY
        st.write("Hasil K:")
        for chunk_key in bin_chunks_key:
            st.write(chunk_key)

    # Meminta input dari pengguna untuk PLAINTEXT
    plaintext = st.text_input("Masukkan PLAINTEXT Anda:")

    if plaintext:
        # Mengubah PLAINTEXT menjadi representasi biner
        bin_plaintext = string_to_bin(plaintext)

        # Memisahkan string biner PLAINTEXT menjadi blok 8 bit
        bin_chunks_plaintext = list(chunks(bin_plaintext, 8))

        # Mencetak blok 8 bit untuk PLAINTEXT
        st.write("Hasil P:")
        for chunk_plaintext in bin_chunks_plaintext:
            st.write(chunk_plaintext)

if __name__ == "__main__":
    main()
