def enskripsi_blocking(block, key):
    return ''.join(chr((ord(char) + key) % 256) for char in block)

def deskripsi_blocking(block, key):
    return ''.join(chr((ord(char) - key) % 256) for char in block)

def pad_plaintext(plaintext, block_size):
    padding_length = block_size - (len(plaintext) % block_size)
    return plaintext + (' ' * padding_length)

def teks_enskripsi(plaintext, block_size, key):
    padded_text = pad_plaintext(plaintext, block_size)
    encrypted_blocks = [
        enskripsi_blocking(padded_text[i:i + block_size], key)
        for i in range(0, len(padded_text), block_size)
    ]
    return ''.join(encrypted_blocks)

def teks_deskripsi(encrypted_text, block_size, key):
    decrypted_blocks = [
        deskripsi_blocking(encrypted_text[i:i + block_size], key)
        for i in range(0, len(encrypted_text), block_size)
    ]
    return ''.join(decrypted_blocks).strip()

def main():
    block_size = 5
    key = 3  

    while True:
        print("\n=== Program Enkripsi dan Dekripsi ===")
        print("1. Masukkan plaintext untuk dienskripsi")
        print("2. Keluar")
        choice = input("Pilih opsi (1/2): ")

        if choice == "1":
            plaintext = input("\nMasukkan plaintext: ")
            encrypted_text = teks_enskripsi(plaintext, block_size, key)
            print("\nHasil Enkripsi: ", encrypted_text)

            # Pilihan setelah enkripsi
            while True:
                print("\nApakah Anda ingin:")
                print("1. Melanjutkan proses dekripsi")
                print("2. Masukkan plaintext baru")
                sub_choice = input("Pilih opsi (1/2): ")

                if sub_choice == "1":
                    decrypted_text = teks_deskripsi(encrypted_text, block_size, key)
                    print("\nHasil Dekripsi: ", decrypted_text)
                    break
                elif sub_choice == "2":
                    break
                else:
                    print("Pilihan tidak valid. Silakan pilih lagi.")
        elif choice == "2":
            print("\nTerima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih lagi.")

# Jalankan program
main()
