def konversiascii(input_string):
    ascii_values = []
    for char in input_string:
        ascii_value = ord(char)
        ascii_values.append(ascii_value)
    return ascii_values
input_string = input("Masukkan string: ")
hasil = konversiascii(input_string)
print("Nilai ASCII dari string:", hasil)