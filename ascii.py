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
    my_string = st.text_input("Masukkan string Anda:")

    if my_string:
        # Mengubah string menjadi representasi biner
        bin_string = string_to_bin(my_string)

        # Memisahkan string biner menjadi blok 8 bit
        bin_chunks = list(chunks(bin_string, 8))

        # Mencetak blok 8 bit
        st.write("Hasil:")
        for chunk in bin_chunks:
            st.write(chunk)

if __name__ == "__main__":
    main()
