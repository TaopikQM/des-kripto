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

def chunks(s, n):
    """Produce `n`-character chunks from `s`."""
    for start in range(0, len(s), n):
        yield s[start:start+n]

def main():
    st.title("String to Binary Converter / DES Key Generation")

    # Memasukkan tombol refresh
    if st.button("Refresh"):
        st.caching.clear_cache()

    # Meminta input dari pengguna untuk String atau DES Key Generation
    my_string = st.text_input("Masukkan String atau PLAINTEXT Anda:")

    if my_string:
        # Mengubah String menjadi representasi biner
        bin_string = string_to_bin(my_string)

        if len(bin_string) == 64:
            # Jika panjang bin_string sudah 64, langsung ke tahapan DES Key Generation
            st.subheader("Tahapan DES Key Generation")

            # Membuat instance DES dengan kunci
            my_des = DES(bin_string)

            # Menerapkan Permutasi Pilihan 1 ke PLAINTEXT
            permuted_plaintext = my_des.permuted_choice_1(my_des.key)

            # Menampilkan PLAINTEXT setelah permutasi
            print("Plaintext setelah PC-1:", permuted_plaintext)
             # Menampilkan PLAINTEXT setelah permutasi 8BIT
            st.write("PC-1 per 8 bit:", " ".join([permuted_plaintext[i:i+8] for i in range(0, len(permuted_plaintext), 8)]))


            # Menampilkan tahapan C0 dan D0
            st.subheader("Tahapan C0 dan D0")
            C0, D0 = my_des.permuted_choice_1(my_des.key)[:28], my_des.permuted_choice_1(my_des.key)[28:]
            st.write("C0:", C0)
            C0_chunks = list(chunks(C0, 8))
            st.write("C0 per 8 bit:", " ".join(C0_chunks))
            st.write("D0:", D0)
            D0_chunks = list(chunks(D0, 8))
            st.write("D0 per 8 bit:", " ".join(D0_chunks))


            # Menampilkan tahapan CD1-16
            st.subheader("Tahapan CD1-16")
            CD_list = []
            for round_number in range(16):
                # Melakukan pergeseran bit pada C0 dan D0 untuk setiap ronde
                C0 = my_des.shift(C0, [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1], round_number)
                D0 = my_des.shift(D0, [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1], round_number)
                CD = C0 + D0
                CD_list.append(CD)
                st.write(f"CD{round_number+1}:", CD)
                st.write(f"CD{round_number+1}  per 8 bit:", ' '.join(list(chunks(CD, 8))))

         

                # Membuat list untuk menyimpan K
                # Menampilkan tahapan CD1-16
                st.subheader("Tahapan K1-16")
                K_list = []
                for round_number in range(16):
                    # Melakukan pergeseran bit pada PLAINTEXT untuk setiap ronde
                    permuted_plaintext = my_des.shift(permuted_plaintext, shift_table, round_number)
        
                    # Menerapkan Permutasi Pilihan 2 ke PLAINTEXT dan menyimpannya dalam K_list
                    K = my_des.permuted_choice_2(permuted_plaintext)
                    K_list.append(K)
                    st.write(f"K{round_number+1}:", K_list[round_number])
        
                    st.write(f"K{round_number+1} per 8 bit:", ' '.join(list(chunks(K, 8))))
        

if __name__ == "__main__":
    main()
