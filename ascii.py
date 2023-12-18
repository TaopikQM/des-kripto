import streamlit as st

class DES:
    def __init__(self, key):
        self.key = key

    def permuted_choice_1(self, key):
        # Tabel Permutasi Pilihan 1 (PC-1)
        PC_1 = [57, 49, 41, 33, 25, 17, 9,
                1, 58, 50, 42, 34, 26, 18,
                10, 2, 59, 51, 43, 35, 27,
                19, 11, 3, 60, 52, 44, 36,
                63, 55, 47, 39, 31, 23, 15,
                7, 62, 54, 46, 38, 30, 22,
                14, 6, 61, 53, 45, 37, 29,
                21, 13, 5, 28, 20, 12, 4]
        permuted_key = ""
        for index in PC_1:
            permuted_key += key[index-1]
        return permuted_key

    def permuted_choice_2(self, key):
        # Tabel Permutasi Pilihan 2 (PC-2)
        PC_2 = [14, 17, 11, 24, 1, 5,
                3, 28, 15, 6, 21, 10,
                23, 19, 12, 4, 26, 8,
                16, 7, 27, 20, 13, 2,
                41, 52, 31, 37, 47, 55,
                30, 40, 51, 45, 33, 48,
                44, 49, 39, 56, 34, 53,
                46, 42, 50, 36, 29, 32]

        permuted_key = ""
        for index in PC_2:
            permuted_key += key[index-1]
        return permuted_key

    def shift(self, bit_string, shift_table, round_number):
        # Melakukan pergeseran bit sesuai dengan tabel iterasi
        return bit_string[shift_table[round_number]:] + bit_string[:shift_table[round_number]]

def string_to_bin(input):
    return ''.join(format(ord(i), '08b') for i in input)

def main():
    st.title("String to Binary Converter / DES Key Generation")

    # Pilihan untuk memilih antara String to Binary atau DES Key Generation
    option = st.radio("Pilih operasi:", ["String to Binary", "DES Key Generation"])

    if option == "String to Binary":
        # Meminta input dari pengguna untuk String
        my_string = st.text_input("Masukkan String Anda:")

        if my_string:
            # Mengubah String menjadi representasi biner
            bin_string = string_to_bin(my_string)

            # Memisahkan string biner menjadi blok 8 bit
            bin_chunks = list(chunks(bin_string, 8))

            # Mencetak blok 8 bit
            st.write("Hasil:")
            for chunk in bin_chunks:
                st.write(chunk)
    elif option == "DES Key Generation":
        # Meminta input dari pengguna untuk PLAINTEXT
        plaintext = st.text_input("Masukkan PLAINTEXT Anda:")

        if plaintext:
            # Membuat instance DES dengan kunci
            my_des = DES(plaintext)

            # Menerapkan Permutasi Pilihan 1 ke PLAINTEXT
            permuted_plaintext = my_des.permuted_choice_1(plaintext)

            # Menampilkan PLAINTEXT setelah permutasi
            st.write("PLAINTEXT setelah PC-1:", permuted_plaintext)

            # Memisahkan PLAINTEXT menjadi per 8 bit
            plaintext_8bit = [permuted_plaintext[i:i+8] for i in range(0, len(permuted_plaintext), 8)]
            st.write("PLAINTEXT per 8 bit:", plaintext_8bit)

            # Tabel iterasi untuk pergeseran bit
            shift_table = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

            # Membuat list untuk menyimpan K
            K_list = []
            for round_number in range(16):
                # Melakukan pergeseran bit pada PLAINTEXT untuk setiap ronde
                permuted_plaintext = my_des.shift(permuted_plaintext, shift_table, round_number)

                # Menerapkan Permutasi
