import streamlit as st

class DES:
    def __init__(self, key):
        self.key = key

    def permuted_choice_1(self, key):
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
        return bit_string[shift_table[round_number]:] + bit_string[:shift_table[round_number]]

def string_to_bin(input):
    return ''.join(format(ord(i), '08b') for i in input)

def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

def main():
    st.title("String to Binary Converter / DES Key Generation")

    if st.button("Refresh"):
        st.caching.clear_cache()

    my_string = st.text_input("Masukkan String atau PLAINTEXT Anda:")

    if my_string:
        # Menampilkan hasil ASCII dari string yang dimasukkan
        st.subheader("Hasil ASCII:")
        ascii_result = ' '.join([format(ord(char), '08b') + f" ({char})" for char in my_string])
        st.write(ascii_result)

        bin_string = string_to_bin(my_string)

        if len(bin_string) == 64:
            st.subheader("Tahapan DES Key Generation")

            my_des = DES(bin_string)

            permuted_plaintext = my_des.permuted_choice_1(my_des.key)

            st.write("PC-1 per 8 bit:", " ".join(list(chunks(permuted_plaintext, 8))))

            st.subheader("Tahapan C0 dan D0")
            C0, D0 = my_des.permuted_choice_1(my_des.key)[:28], my_des.permuted_choice_1(my_des.key)[28:]
            st.write("C0 per 8 bit:", " ".join(list(chunks(C0, 8))))
            st.write("D0 per 8 bit:", " ".join(list(chunks(D0, 8))))

            st.subheader("Tahapan CD1-16")
            CD_list = []
            for round_number in range(16):
                C0 = my_des.shift(C0, [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1], round_number)
                D0 = my_des.shift(D0, [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1], round_number)
                CD = C0 + D0
                CD_list.append(CD)
                st.write(f"CD{round_number+1} per 8 bit:", ' '.join(list(chunks(CD, 8))))

            st.subheader("Tahapan K1-16")
            K_list = []
            for round_number in range(16):
                permuted_plaintext = my_des.shift(permuted_plaintext, [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1], round_number)
                K = my_des.permuted_choice_2(permuted_plaintext)
                K_list.append(K)
                st.write(f"K{round_number+1} per 8 bit:", ' '.join(list(chunks(K, 8))))

if __name__ == "__main__":
    main()
