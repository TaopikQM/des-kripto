import streamlit as st

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

def string_to_bin(input):
    return ''.join(format(ord(i), '08b') for i in input)

def main():
    st.title("String to Binary Converter")

    # Meminta input dari pengguna
    my_string = st.text_input("Masukkan KEY Anda:")

    if my_string:
        # Mengubah string menjadi representasi biner
        bin_string = string_to_bin(my_string)

        # Memisahkan string biner menjadi blok 8 bit
        bin_chunks = list(chunks(bin_string, 8))

        # Mencetak blok 8 bit
        st.write("Hasil K:")
        for chunk in bin_chunks:
            st.write(chunk)

     # Meminta input dari pengguna
    my_string = st.text_input("Masukkan PLAINTEXT Anda:")

     if my_stringG:
        # Mengubah string menjadi representasi biner
        bin_stringG = string_to_bin(my_stringG)

        # Memisahkan string biner menjadi blok 8 bit
        bin_chunksG = list(chunks(bin_stringG, 8))

        # Mencetak blok 8 bit
        st.write("Hasil P:")
        for chunkG in bin_chunksG:
            st.write(chunkG)
if __name__ == "__main__":
    main()
