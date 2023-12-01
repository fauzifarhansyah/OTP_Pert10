def kodeascii(ascii_code):
    return chr(ascii_code)
ascii_code = int(input("Masukkan kode ASCII: "))
character = kodeascii(ascii_code)
print(f"Karakter untuk kode ASCII {ascii_code} adalah '{character}'")