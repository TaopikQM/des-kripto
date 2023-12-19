import streamlit as st

 # S-Box Tables
S_Boxes = [
    # S1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

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
     
    def initial_permutation(self, plaintext):
        # Tabel Initial Permutation (IP)
        IP = [58, 50, 42, 34, 26, 18, 10, 2,
              60, 52, 44, 36, 28, 20, 12, 4,
              62, 54, 46, 38, 30, 22, 14, 6,
              64, 56, 48, 40, 32, 24, 16, 8,
              57, 49, 41, 33, 25, 17, 9, 1,
              59, 51, 43, 35, 27, 19, 11, 3,
              61, 53, 45, 37, 29, 21, 13, 5,
              63, 55, 47, 39, 31, 23, 15, 7]
        permuted_plaintext = ""
        for index in IP:
            permuted_plaintext += plaintext[index - 1]
        return permuted_plaintext

    def expansion(self, bit_string):
        # Tabel Ekspansi (E)
        E = [32, 1, 2, 3, 4, 5,
             4, 5, 6, 7, 8, 9,
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17,
             16, 17, 18, 19, 20, 21,
             20, 21, 22, 23, 24, 25,
             24, 25, 26, 27, 28, 29,
             28, 29, 30, 31, 32, 1]
        expanded_bit_string = ""
        for index in E:
            expanded_bit_string += bit_string[index - 1]
        return expanded_bit_string

    def xor(self, bit_string1, bit_string2):
        # Melakukan operasi XOR pada dua string bit
        return ''.join(str(int(b1) ^ int(b2)) for b1, b2 in zip(bit_string1, bit_string2))

    def permutation(self, bit_string):
        # Tabel Fungsi P
        P = [
            [16, 7, 20, 21],
            [29, 12, 28, 17],
            [1, 15, 23, 26],
            [5, 18, 31, 10],
            [2, 8, 24, 14],
            [32, 27, 3, 9],
            [19, 13, 30, 6],
            [22, 11, 4, 25]
        ]
        permuted_bit_string = ""
        for row in P:
            for index in row:
                permuted_bit_string += bit_string[index - 1]
        return permuted_bit_string

def s_box_substitution(bit_string, s_box_index):
    # Pastikan bit_string memiliki panjang minimal 6 karakter
    if len(bit_string) < 6:
        raise ValueError("bit_string harus memiliki panjang minimal 6 karakter")
    
    # Lakukan substitusi sesuai dengan indeks yang diinginkan
    row = int(bit_string[0] + bit_string[5], 2)
    col = int(bit_string[1:5], 2)
        
    return format(S_Boxes[s_box_index][row][col], '04b')
 
def string_to_bin(input):
    return ''.join(format(ord(i), '08b') for i in input)

def string_to_biin(input):
    return ''.join(format(ord(i), '08b') for i in input)
       
def chunks(s, n):
    for start in range(0, len(s), n):
        yield s[start:start+n]

def main():
    st.title("String to Binary Converter / DES Key Generation")

    if st.button("Refresh"):
       
        st.write("Proses caching akan dihapus.")
    
        # Menghapus cache (pastikan ini diperlukan di sini)
        st.caching.clear_cache()

    my_string = st.text_input("Masukkan String atau KEY Anda:")

    if my_string:
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

 #TAHAPAN PLAITEXT KE BINNER ASCII
            st.title("String to Binary Converter / DES PLAINTEXT Generation")
        
            my_string = st.text_input("Masukkan PLAINTEXT Anda:")
        
            if my_string:
                # Menampilkan hasil ASCII dari string yang dimasukkan
                st.subheader("Hasil ASCII:")
                ascii_result = ' '.join([format(ord(char), '08b') + f" ({char})" for char in my_string])
                st.write(ascii_result)

                bin_string = string_to_bin(my_string)  # Pastikan string_to_bin telah didefinisikan
                if len(bin_string) == 64:  # Gunakan bin_string bukan my_string
                    st.subheader("Tahapan DES PLAINTEXT Generation")

                    my_des = DES(bin_string)
                    my_des.plaintext = bin_string  # Pastikan plaintext diatur dengan benar

                    # Menerapkan Initial Permutation ke plaintext
                    permuted_plaintext = my_des.initial_permutation(my_des.plaintext)

                    # Menampilkan plaintext setelah Initial Permutation
                    st.subheader("Plaintext setelah IP:")
                    st.write(permuted_plaintext)

                    # Memisahkan permuted_plaintext dengan spasi setiap 8 bit
                    permuted_plaintext_spaced = ' '.join([permuted_plaintext[i:i + 8] for i in range(0, len(permuted_plaintext), 8)])
                    st.subheader("Plaintext setelah IP per 8 bit (dengan spasi):")
                    st.write(permuted_plaintext_spaced)
        
                    # Split plaintext into L0 and R0
                    L0, R0 = permuted_plaintext[:len(permuted_plaintext)//2], permuted_plaintext[len(permuted_plaintext)//2:]
        
                    # Set R0 to L1
                    L1 = R0
        
                    # Expand R0 with E table
                    expanded_R0 = my_des.expansion(R0)

                    # Display L0, R0, L1, E(R0) dengan spasi setiap 8 bit

                    # Display L0, R0, L1, E(R0)
                    st.subheader("L0:")
                    st.write(L0)
                    st.subheader("L0 per 8 bit:")
                    st.write(' '.join([L0[i:i + 8] for i in range(0, len(L0), 8)]))
                    st.subheader("R0:")
                    st.write(R0)
                    st.subheader("R0 per 8 bit:")
                    st.write(' '.join([R0[i:i + 8] for i in range(0, len(R0), 8)]))
                    st.subheader("L1:")
                    st.write(L1)
                    st.subheader("L1 per 8 bit:")
                    st.write(' '.join([L1[i:i + 8] for i in range(0, len(L1), 8)]))
                    st.subheader("E(R0):")
                    st.write(expanded_R0)
                    st.subheader("E(R0 per 8 bit):")
                    st.write(' '.join([expanded_R0[i:i + 8] for i in range(0, len(expanded_R0), 8)]))
                   
                    key = K_list[0]
        
                    # Input key in binary form from the user
                    my_des.key = st.text_input("Enter the key (K1):", key)

                    # XOR R0 after expansion with the key
                    xor_result = my_des.xor(expanded_R0, my_des.key)
                    st.subheader("XOR Result (E(R0) and Key):")
                    st.write(xor_result)

                    xor_blocks = []

                    # Pemisahan menjadi 8 blok dengan panjang 6 bit
                    for i in range(0, len(xor_result), 6):
                        xor_blocks.append(xor_result[i:i+6])
                    
                    # Tampilkan hasil blok-blok
                    for i, block in enumerate(xor_blocks):
                        st.write(f"Block {i + 1}: {block}")

                    #INI SETELAH SBLOCK
                    s_box_results = []
                    # lakukan substitusi S-Box pada setiap blok
                    for i, block in enumerate(xor_blocks):
                        s_box_result = s_box_substitution(block, i % 8)  # gunakan modulo 8 untuk memastikan indeks berada dalam rentang 0-7
                        st.write(f"Block {i + 1}: {block} -> S-Box Substitution: {s_box_result}")
                   
                    # gabungkan semua hasil menjadi satu baris dengan spasi sebagai pemisah
                    single_line = ' '.join(s_box_results)
                    st.write(single_line)
                    print("Blok setelah substitusi:", blocks)
                    
                    # Menggabungkan semua blok menjadi satu string bit
                    substituted_result = "".join(blocks)
                    print("Hasil akhir setelah substitusi:", substituted_result)
                    # Split XOR result into 6-bit blocks
                    blocks = [xor_result[i:i + 6] for i in range(0, len(xor_result), 6)]
                    
                    # Apply S-box substitution to each 6-bit block
                    s_box_substituted_blocks = [my_des.s_box_substitution(block, s_box_index) for block in blocks]
                    
                    # Display the S-box substituted blocks
                    
                    st.subheader("Blocks after S-box substitution:")
                    for i, block in enumerate(s_box_substituted_blocks, start=1):
                        st.write(f"Block {i}: {block}")
                    substituted_blocks = []
                    for block_number in range(len(blocks)):
                        block = blocks[block_number]
                        row = int(block[0] + block[5], 2)  # Ambil bit pertama dan terakhir untuk baris
                        col = int(block[1:5], 2)  # Ambil 4 bit tengah untuk kolom
                        substituted_value = S_Boxes[block_number][row][col]  # Ambil nilai substitusi dari tabel S-box
                        substituted_blocks.append(format(substituted_value, '04b'))  # Konversi nilai menjadi biner 4-bit dan tambahkan ke daftar
                
                    # Tampilkan hasil substitusi S-box
                    st.subheader("Blocks after S-box substitution:")
                    st.write(" ".join(substituted_blocks))
                    #blocks = []
                   # Substitusi S-box untuk setiap blok
                    #for i in range(len(blocks)):
                     #   block = blocks[i]
                      #  substituted_block = "".join([my_des.s_box_substitution(block[j:j + 6]) for j in range(0, len(block), 6)])
                       # blocks[i] = substituted_block
                    

                    # Split hasil substitusi S-box menjadi 6-bit blok
                    blocks_after_substitution = [substituted_block[i:i + 6] for substituted_block in blocks for i in range(0, len(substituted_block), 6)]
                    
                    # Tampilkan semua blok setelah substitusi S-box dalam satu baris
                    st.subheader("Blocks after S-box substitution:")
                    st.write(" ".join(blocks_after_substitution))
                    
                    # Split XOR result into 6-bit blocks
                    xor_blocks = [xor_result[i:i + 6] for i in range(0, len(xor_result), 6)]
                    
                    # Tampilkan semua blok setelah operasi XOR dalam satu baris
                    st.subheader("Blocks after XOR:")
                    st.write(" ".join(xor_blocks))

                    
                    # Split hasil substitusi menjadi 6-bit blok
                    blocks = [blocks[i:i + 6] for i in range(0, len(blocks), 6)]
                    
                    # Tampilkan semua blok dalam satu baris
                    st.subheader("Blocks after S-box substitution:")
                    st.write(" ".join(blocks))
                    # Split XOR result into 6-bit blocks
                    blocks = [xor_result[i:i + 6] for i in range(0, len(xor_result), 6)]
        
                    # Display all blocks in one line
                    st.subheader("Blocks after XOR:")
                    st.write(" ".join(blocks))
        
                    # Display each block
                    for i, block in enumerate(blocks):
                        st.write(f"Block {i+1}:", block)
        
                    # Substitute each block with the corresponding S-Box
                    for i, block in enumerate(blocks):
                        blocks[i] = my_des.s_box_substitution(block, S_Boxes[i])
        
                    # Display blocks after substitution
                    st.subheader("Blocks after substitution:")
                    st.write(blocks)
        
                    # Combine all blocks into one bit string
                    substituted_result = "".join(blocks)
        
                    # Display substitution result and permutation result
                    st.subheader("Substitution Result:")
                    st.write(substituted_result)
        
                    # Permute the result with the P table
                    permuted_result = my_des.permutation(substituted_result)
        
                    st.subheader("Permutation Result:")
                    st.write(permuted_result)
        
                    # Split permuted_result into 4-bit chunks
                    permuted_result_4bit = [permuted_result[i:i + 4] for i in range(0, len(permuted_result), 4)]
        
                    st.subheader("Permutation Result per 4 bits:")
                    st.write(permuted_result_4bit)
        
                    # XOR permuted_result with L0
                    xor_result = my_des.xor(permuted_result, L0)
        
                    st.subheader("XOR Result (Permutation and L0):")
                    st.write(xor_result)
        
                    # Split XOR result into 4-bit chunks
                    xor_result_4bit = [xor_result[i:i + 4] for i in range(0, len(xor_result), 4)]
        
                    st.subheader("XOR Result per 4 bits:")
                    st.write(xor_result_4bit)
        
                    # Apply P-Box to the XOR result
                    final_result = my_des.permutation(xor_result)
        
                    st.subheader("Final Result after P-Box:")
                    st.write(final_result)
        
                    # Split final_result into 4-bit chunks
                    final_result_4bit = [final_result[i:i + 4] for i in range(0, len(final_result), 4)]
        
                    st.subheader("Final Result after P-Box per 4 bits:")
                    st.write(final_result_4bit)
        
                    # Set L1 to R1
                    R1 = L1
        
                    # Display L1 and R1
                    st.subheader("L1:")
                    st.write(L1)
                    st.subheader("R1:")
                    st.write(R1)
        
                    # XOR R1 with the result after P-Box
                    new_L1 = my_des.xor(R1, final_result)
        
                    st.subheader("L1 after XOR:")
                    st.write(new_L1)
        
                    # Display the final encryption result
                    ciphertext = R1 + new_L1
                    st.subheader("Final Encryption Result:")
                    st.write(ciphertext)


if __name__ == "__main__":
    main()
