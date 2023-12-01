def konversiascii(input_string):
    ascii_values = []
    for char in input_string:
        ascii_value = ord(char)
        ascii_values.append(ascii_value)
    return ascii_values

def konversibiner(input_string):
    binary_values = []
    for vhar in input_string:
        binary_value = bin(char)[2:]
        binary_values.append(binary_value)
    return binary_values

input_string = input("Masukkan string: ")
ascii_values = konversiascii(input_string)
hasil = konversibiner(ascii_values)
print("Nilai biner dari string:", hasil)